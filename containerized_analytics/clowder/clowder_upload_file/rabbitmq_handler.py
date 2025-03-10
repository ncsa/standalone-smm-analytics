import json
import os
import traceback

import pika
import requests
import writeToS3 as s3

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')


def get_config_json(config_url):
    # download config data to json
    try:
        localPath, filename = s3.downloadUrlToDisk(config_url)
        with open(os.path.join(localPath, filename), 'r') as f:
            return json.load(f)
    except:
        print('Cannot find configuration file in the remote storage!')
        return None


def rabbitmq_handler(ch, method, properties, body):

    clowder_base_url = os.getenv('CLOWDER_BASE_URL', 'https://clowder.smm.ncsa.illinois.edu/')

    try:
        # basic fields
        event = json.loads(body)
        auth = (event['username'], event['password'])
        dataset_id = event['payload']['dataset_id']

        if 'configuration' in event['payload'].keys():
            config_url = event['payload']['configuration']
            config_json = get_config_json(config_url)
        else:
            config_json = None

        # upload files
        file_urls = []
        for file in event['payload']['files']:
            try:
                localPath, filename = s3.downloadUrlToDisk(file['url'])
            except:
                raise ValueError('Cannot find file: in the remote storage!')

            r = requests.post(
                clowder_base_url + 'api/uploadToDataset/' + dataset_id +
                '?extract=true',
                files=[('File', open(os.path.join(localPath, filename), 'rb'))],
                auth=auth)

            if r.status_code != 200:
                raise ValueError("cannot upload these files to dataset: " +
                                 dataset_id + ". error:" + r.text)
            else:
                file_urls.append(clowder_base_url + "files/" + r.json()['id'])

            # add config file to metadata (default) if config file exists
            if config_json is not None:
                config_metadata_r = requests.post(clowder_base_url + 'api/files/' + r.json()['id'] + '/metadata',
                                                  data=json.dumps(config_json),
                                                  headers={"Content-Type": "application/json"},
                                                  auth=auth)
                if config_metadata_r.status_code != 200:
                    raise ValueError('cannot add configuration metadata to this file: ' + r.json()['id'] + ". error: " +
                                     config_metadata_r.text)

            # add tags
            if 'tags' in file.keys():
                tag_payload = json.dumps({'tags': file['tags']})
                tag_r = requests.post(clowder_base_url + 'api/files/' + r.json()['id'] + '/tags',
                                      data=tag_payload,
                                      headers={"Content-Type": "application/json"},
                                      auth=auth)
                if tag_r.status_code != 200:
                    raise ValueError('cannot add tags to this file: ' + r.json()['id'] + ". error: " + tag_r.text)

            # add metadata
            if 'metadata' in file.keys():
                metadata_payload = json.dumps(file['metadata'])
                metadata_r = requests.post(clowder_base_url + 'api/files/' + r.json()['id'] + '/metadata',
                                           data=metadata_payload,
                                           headers={"Content-Type": "application/json"},
                                           auth=auth)
                if metadata_r.status_code != 200:
                    raise ValueError('cannot add metadata to this file: ' + r.json()['id'] + ". error: " +
                                     metadata_r.text)

            # add description
            if 'descriptions' in file.keys():
                description_payload = json.dumps({'description': file['descriptions']})
                description_r = requests.put(clowder_base_url + 'api/files/' + r.json()['id'] + '/updateDescription',
                                             data=description_payload,
                                             headers={"Content-Type": "application/json"},
                                             auth=auth)
                if description_r.status_code != 200:
                    raise ValueError(
                        'cannot add descriptions to this file: ' + r.json()['id'] + ". error: " + description_r.text)

        resp = {'info': 'You have successfully uploaded all the files to your specified dataset!',
                'ids': file_urls}

    except BaseException as e:
        resp = {
            'ERROR':
                {
                    'message': str(e),
                    'traceback': traceback.format_exc()
                }
        }

    # reply to the sender
    ch.basic_publish(exchange="",
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=json.dumps(resp))

    return resp


if __name__ == '__main__':
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST, 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # pass the queue name in environment variable
    queue = os.environ['QUEUE_NAME']

    channel.queue_declare(queue=queue)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue, on_message_callback=rabbitmq_handler, auto_ack=True)
    channel.start_consuming()
