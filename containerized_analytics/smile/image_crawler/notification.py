import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import urllib.parse

import contextlib

try:
    from urllib.parse import urlencode

except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen

except ImportError:
    from urllib2 import urlopen


def reformat_sessionURL(sessionURL):
    # hubzero tool have sessionURL = https://{host}/session/{sessionID}/originalPath
    # standalone smile have sessionURL = https://{host}/originalPath
    # Split the URL by '/' and remove the last part
    url_parts = sessionURL.split('/')
    url_parts.pop()

    # Append "/history" to the URL
    url_parts.append("history")

    # Reconstruct the URL
    new_sessionURL = '/'.join(url_parts)

    return new_sessionURL


def make_tiny(url):
    try:
        request_url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': url})
        with contextlib.closing(urlopen(request_url)) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        # If there is an error (e.g., network issue or TinyURL service is down), return the original URL
        return url


def notification(toaddr, case, filename, links, sessionURL):
    # toaddr -- email address to send to
    # text content to send
    # subject
    host = os.environ.get('EMAIL_HOST')
    port = os.environ.get('EMAIL_PORT', 25)
    fromaddr = os.environ.get('EMAIL_FROM_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')

    if host is not None and host != "" and \
            port is not None and port != "" and \
            fromaddr is not None and fromaddr != "":
        # map the fpath component to History panel names
        # local/NLP/sentiment/xxxxxxxxxxxxxxxxxxxxxxxx/ => [local,nlp,sentiment,xxxx,space]
        # [local, GraphQL, reddit-post, aww, space]
        # 0         1          2        3
        if filename != '':
            fpath = filename.split('/')

            if fpath[1] == 'GraphQL':
                fpath[1] = 'Social Media Data'
            elif fpath[1] == 'NLP':
                fpath[1] = 'Nature Language Processing'
            elif fpath[1] == 'ML':
                fpath[1] = 'Machine Learning ML'
            elif fpath[1] == 'NW':
                fpath[1] = 'Network Visualization and Analysis'

            if fpath[2] == 'reddit-Post':
                fpath[2] = 'Subreddit Posts Title'
            elif fpath[2] == 'reddit-Historical-Post':
                fpath[2] = 'Reddit Historical Post'
            elif fpath[2] == 'reddit-Search':
                fpath[2] = 'Reddit Search Posts Title'
            elif fpath[2] == 'sentiment':
                fpath[2] = 'Sentiment Analysis'
            elif fpath[2] == 'preprocessing':
                fpath[2] = 'NLP Preprocessing'
            elif fpath[2] == 'networkx':
                fpath[2] = 'Python NetworkX'
            elif fpath[2] == 'classification':
                fpath[2] = 'Text Classification'
        else:
            fpath = []

        if len(fpath) >= 3:
            if case == 0 or case == 'comment-fail':
                html = f"""
                <html> 
                    <head></head>
                    <body style="font-size:15px;font-fiamily:'Times New Roman', Times, serif;">
                <div>
                            <p>Dear user (session ID: {fpath[0]}),</p>
                    <p>Your Reddit Comment collection has been terminated.</p>
                    <p>We are using the <b>id</b> and <b>permalink</b> from your Reddit Submission dataset
                    to collect comments and replies. It is most likely you have provide an incomplete Reddit Submission dataset missing these two fields.</p>
                    <p>Please try to reproduce the Reddit Submission with <b>id</b> and <b>permalink</b>, or switch to another dataset.</p>
                    <a href="{sessionURL}">Go to your session...</a>
                            <br>
                            <p>Best Regards,</p>
                            <p>Social Media Macroscope - SMILE </p>
                </div>
                    </body>
                </html>
                """
                subject = 'Your Reddit Comment collection has failed...'
            elif case == 1 or case == 'comment-terminate':
                html = f"""<html> 
                            <head></head>
                            <body style="font-size:15px;font-fiamily:'Times New Roman', Times, serif;">
                                <div>
                                    <p>Dear user (session ID: {fpath[0]}),</p>
                                    <p>Your Reddit Comment collection is exceeding 400 Megabyte, and is terminated due to lack of disk space.</p>
                                    <ul>
                                        <li>You have requested comments and replies for the Reddit Submission (
                                        Post):<b>{fpath[3]}</b>. The partial comments we manage to collect 
                                        and save will be compressed for you in an .zip file named <a href="{make_tiny(links)}">
                                        {fpath[3]}-comments.zip</a> (click)</li>    
                                        <li>In order to download this file, you need to first locate the original submission in the <b>Past Results</b> page in SMILE.
                                           <a href="{reformat_sessionURL(sessionURL)}">Go to your session.</a> 
                                        <ul>
                                            <li>Go to <b>Past Results</b></li> 
                                            <li>--> under <b>{fpath[1]}</b></li> 
                                            <li>--> click <b>{fpath[2]}</b></li> 
                                            <li>--> then find <b>{fpath[3]}</b></li> 
                                            <li>--> click <b>VIEW</b></li> 
                                            <li>--> in the <b>Overview</b> table under the <b>downloadables</b> column, you will find these comments in a zip file.</li>
                                        </ul>
                                    <ul>
                                    <br>
                                    <p>Best Regards,</p>
                                    <p>Social Media Macroscope - SMILE </p>
                                </div>
                            </body>
                    </html>"""
                subject = 'Your Reddit Comment collection has been terminated...'
            elif case == 2 or case == 'comment-success':
                html = f"""<html> 
                            <head></head>
                            <body style="font-size:15px;font-fiamily:'Times New Roman', Times, serif;">
                                <div>
                                    <p>Dear user (session ID: {fpath[0]}),</p>
                                    <p>Your Reddit Comment collection is ready for you!</p>
                                    <ul>
                                        <li>You have requested comments and replies for the Reddit Submission (
                                        Post):<b>{fpath[3]}</b>. It will be compressed for you in an .zip file named 
                                        <a href="{make_tiny(links)}">{fpath[3]}-comments.zip</a></li>    
                                        <li>In order to download this file, you need to first locate the original submission in the <b>Past Results</b> page in SMILE.
                                        <a href="{reformat_sessionURL(sessionURL)}">Go to your session.</a>
                                        <ul>
                                            <li>Go to <b>Past Results</b></li> 
                                            <li>--> under <b>{fpath[1]}</b></li> 
                                            <li>--> click <b>{fpath[2]}</b></li> 
                                            <li>--> then find <b>{fpath[3]}</b></li>
                                            <li>--> click <b>VIEW</b></li> 
                                            <li>--> in the <b>Overview</b> table under the <b>downloadables</b> column, you will find these comments in a zip file.</li>
                                        </ul>
                                    </ul>
                                    <br>
                                    <p>Best Regards,</p>
                                    <p>Social Media Macroscope - SMILE </p>
                                </div>
                            </body>
                    </html>"""
                subject = 'Your Reddit Comment collection is completed!'
            elif case == 3 or case == 'analytics-success':
                list_html = ''
                for key in links.keys():
                    list_html += f'<li><a href="{make_tiny(links[key])}">{key}</a></li>'

                html = f"""<html> 
                            <head></head>
                            <body style="font-size:15px;font-fiamily:'Times New Roman', Times, serif;">
                                <div>
                                    <p>Dear user (session ID:{fpath[0]}),</p>
                                    <p>Your {fpath[2]} results are ready for you! (job ID: {fpath[3]})</p>
                                    <ul>
                                        <li>You can view the visualization and download the results at <b>Past Results</b> page in SMILE. 
                                        <a href="{reformat_sessionURL(sessionURL)}">Go to your session.</a>
                                        <ul>
                                            <li>Go to <b>Past Results</b></li>
                                            <li>--> under <b>{fpath[1]}</b> tab</li>
                                            <li>--> click <b>{fpath[2]}</b></li>
                                            <li>--> then find <b>{fpath[3]}</b></li>
                                            <li>--> click <b>view</b></li>
                                        </ul>
                                        <br>
                                        <li>You can also click the link below to download part of the results:
                                            <ul>{list_html}</ul>
                                        </li>
                                    </ul>
                                    <br>
                                    <p>Best Regards,</p>
                                    <p>Social Media Macroscope - SMILE </p>
                                </div>
                            </body>
                    </html>"""
                subject = f'Your {fpath[2]} computation is completed!'
            else:
                html = None
                subject = None
                print("Invalid case! Skip notification.")

            if html is not None and subject is not None:
                msg = MIMEMultipart('alternative')
                msg['Subject'] = subject
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg.attach(MIMEText(html, 'html'))

                server = smtplib.SMTP(host, int(port))
                server.starttls()
                if password is not None and password != "":
                    server.login(fromaddr, password)
                server.sendmail(fromaddr, toaddr, msg.as_string())
                server.quit()
            else:
                print("Invalid html content! Skip notification.")
        else:
            print("Invalid filepath! Skip notification.")

    else:
        print("Invalid Email host setting! Skip notification.")

