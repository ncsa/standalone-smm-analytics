[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

## Social Media Macroscope Analytics Repository
This repository hosts all the analytics and computation scripts for SMM tools. Short running algorithms with 
small dependency libraries are deployed on [AWS Lambda](https://aws.amazon.com/lambda/), while long running processes with large libraries 
required are deployed on [AWS Batch](https://aws.amazon.com/batch/)

### Setting up nginx
- modify rabbitmg/nginx/nginx.conf to have <<server_name>>:8001
- modify rabiitmg/nginx_wo_ssl/nginx_wo_ssl.conf to have <<server_name>>:8001

## Using Docker Compose (no traefik)
### Set up environment variables
- use the script `docker-compose-smile.sh`
- or manually set following environment variables that start docker-compose with `docker-compose-smile.yml`
- following code block includes the set up for the local directory and this can be modified based on the convenience
- many of them are optional, so some of them can be skipped based on the situation
```angular2html
# system setting
export DOCKERIZED=true

# if use AWS algorithm, then you must use a static IP address
export LOCAL_ALGORITHM=true

# single user version vs multiple users
export SINGLE_USER=false

#set up home directory
export HOME=/your/home/directory

#set server info
export SERVER=smm.server.com

# settings for CILOGON
export CILOGON_CLIENT_ID=<<cilogon id>>
export CILOGON_CLIENT_SECRET=<<cilogon client secret>>
export CILOGON_CALLBACK_URL=<<ci logon callback url>>

export MINIO_URL=http://${SERVER}:9000/
export MINIO_PUBLIC_ACCESS_URL=http://${SERVER}:9000/
export BUCKET_NAME=macroscope-smile
export SMILE_GRAPHQL_URL=http://${SERVER}:5050/graphql

# create mounted volumes on host machine
mkdir -p ${HOME}/smile_data/${BUCKET_NAME}
mkdir -p ${HOME}/smile_user
mkdir -p ${HOME}/smile

export RABBITMQ_URL=amqp://${SERVER}:5672
export RABBITMQ_HOST=${SERVER}
export REDIS_URL=redis://redis:6379

# email notification
#export EMAIL_HOST=<<email host>>
#export EMAIL_PORT=465
#export EMAIL_FROM_ADDRESS=<<email from address>>
#export EMAIL_PASSWORD=<<email password>>

# align with AWS
export AWS_ACCESSKEY=<<aws_accesskey>>
export AWS_ACCESSKEYSECRET=<<aws_accesskeysecret>>

# social media platforms
export REDDIT_CLIENT_ID=<<reddit client id>>
export REDDIT_CLIENT_SECRET=<<reddit client secret>>
export REDDIT_CALLBACK_URL=<<reddit callback url>>
#export TWITTER_CONSUMER_KEY=<<twitter consumer key>>
#export TWITTER_CONSUMER_SECRET=<<twitter consumer secret>>
export TWITTER_V2_CLIENT_ID=<<twitter v2 client id>>
export TWITTER_V2_CLIENT_SECRET=<<twitter v2 client secret>>
export TWITTER_V2_CALLBACK_URL=<<twitter v2 callback url>>

# export
export BOX_CLIENT_ID=<box client id>
export BOX_CLIENT_SECRET=<<box client secret>>
export DROPBOX_CLIENT_ID=<<dropbox client id>>
export DROPBOX_CLIENT_SECRET=<<dropbox client secret>>
export GOOGLE_CLIENT_ID=<<google client id>>
export GOOGLE_CLIENT_SECRET=<<google client secret>>

export CLOWDER_BASE_URL=https://clowder.server.com/
export CLOWDER_GLOBAL_KEY=<<clowder global key>>
```

## Using Docker Compose (with traefik)
- use the script `docker-compose-smile-traefik.sh`
- or manually set the following environment variables then run docker-compose using the `docker-compose-smile-traefik.yml`
- many of them are optional so some of them can be skipped based on the situation
```angular2html
# system setting
export DOCKERIZED=true

# if use AWS algorithm, then you must use a static IP address
export LOCAL_ALGORITHM=true

# single user version vs multiple users
export SINGLE_USER=false

#set up home directory
export HOME=/your/home/directory

#set server info
export SERVER=smm.server.com

# settings for CILOGON
export CILOGON_CLIENT_ID=<<cilogon id>>
export CILOGON_CLIENT_SECRET=<<cilogon client secret>>
export CILOGON_CALLBACK_URL=<<ci logon callback url>>

export MINIO_URL=https://minio-api.${SERVER}
export MINIO_PUBLIC_ACCESS_URL=https://minio-api.${SERVER}
export BUCKET_NAME=macroscope-smile
export SMILE_GRAPHQL_URL=https://graphql.${SERVER}/graphql

# create mounted volumes on host machine
mkdir -p ${HOME}/smile_data/${BUCKET_NAME}
mkdir -p ${HOME}/smile_user
mkdir -p ${HOME}/smile

export RABBITMQ_HOST=${SERVER}
export RABBITMQ_URL=amqp://${SERVER}
export REDIS_URL=redis://redis

# email notification
#export EMAIL_HOST=<<email host>>
#export EMAIL_PORT=465
#export EMAIL_FROM_ADDRESS=<<email from address>>
#export EMAIL_PASSWORD=<<email password>>

# align with AWS
export AWS_ACCESSKEY=<<aws_accesskey>>
export AWS_ACCESSKEYSECRET=<<aws_accesskeysecret>>

# social media platforms
export REDDIT_CLIENT_ID=<<reddit client id>>
export REDDIT_CLIENT_SECRET=<<reddit client secret>>
export REDDIT_CALLBACK_URL=<<reddit callback url>>
#export TWITTER_CONSUMER_KEY=<<twitter consumer key>>
#export TWITTER_CONSUMER_SECRET=<<twitter consumer secret>>
export TWITTER_V2_CLIENT_ID=<<twitter v2 client id>>
export TWITTER_V2_CLIENT_SECRET=<<twitter v2 client secret>>
export TWITTER_V2_CALLBACK_URL=<<twitter v2 callback url>>

# export
export BOX_CLIENT_ID=<box client id>
export BOX_CLIENT_SECRET=<<box client secret>>
export DROPBOX_CLIENT_ID=<<dropbox client id>>
export DROPBOX_CLIENT_SECRET=<<dropbox client secret>>
export GOOGLE_CLIENT_ID=<<google client id>>
export GOOGLE_CLIENT_SECRET=<<google client secret>>

export CLOWDER_BASE_URL=https://clowder.server.com/
export CLOWDER_GLOBAL_KEY=<<clowder global key>>

# start
docker-compose -f docker-compose-smile-traefik.yml -d up

# stop
# docker-compose -f docker-compose-smile.yml down -v

# update latest image from docker hub
# docker-compose -f docker-compose-smile.yml pull

```
Contact us the **[SRTI lab](https://srtilab.techservices.illinois.edu/about/)** if you have any question: <a href="mailto:srti-lab@illinois.edu">srti-lab@illinois.edu</a>
