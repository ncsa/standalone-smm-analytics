[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

## Deploying SMILE
SMILE can be deployed using docker-compose. 
In this repository, there are two ways of deploying it, 
one is using traefik, and the other is a conventional way using nginx.
[Traefik](https://traefik.io/traefik/) is s a modern reverse proxy and 
load balancer that makes deploying microservices easy, and is designed to be 
as simple as possible to operate. 
It integrates with infrastructure components and configures itself automatically and dynamically.

## Using Docker Compose (no traefik)
### Set up environment variables
- use the script [docker-compose-smile.sh](https://github.com/ncsa/standalone-smm-analytics/blob/main/rabbitmq/docker-command-smile.sh)
- or manually set following environment variables that start docker-compose with `docker-compose-smile.yml`
  - environment variable information is in the script
- following code block includes the set up for the local directory and this can be modified based on the convenience
- many of them are optional, so some of them can be skipped based on the situation

## Using Docker Compose (with traefik)
- use the script [docker-compose-smile-traefik.sh](https://github.com/ncsa/standalone-smm-analytics/blob/main/rabbitmq/docker-command-smile-traefik.sh) 
- or manually set the following environment variables then run docker-compose using the `docker-compose-smile-traefik.yml`
- many of them are optional so some of them can be skipped based on the situation

### Optional environment variables
- system setting 
  - DOCKERIZED=true 
- if use AWS algorithm, then you must use a static IP address 
  - LOCAL_ALGORITHM=true
- single user version vs multiple users
  - SINGLE_USER=false 
- settings for CILOGON (this doesn't be needed if SINGLE_USER is true)
  - CILOGON_CLIENT_ID=<<cilogon id>>
  - CILOGON_CLIENT_SECRET=<<cilogon client secret>>
  - CILOGON_CALLBACK_URL=<<ci logon callback url>>
- email notification 
  - EMAIL_HOST=<<email host>>
  - EMAIL_PORT=465 
  - EMAIL_FROM_ADDRESS=<<email from address>>
  - EMAIL_PASSWORD=<<email password>>
- align with AWS 
  - AWS_ACCESSKEY=<<aws_accesskey>>
  - AWS_ACCESSKEYSECRET=<<aws_accesskeysecret>>
- social media platforms (some of these can be optional)
  - REDDIT_CLIENT_ID=<<reddit client id>>
  - REDDIT_CLIENT_SECRET=<<reddit client secret>>
  - REDDIT_CALLBACK_URL=<<reddit callback url>>
  - TWITTER_CONSUMER_KEY=<<twitter consumer key>>
  - TWITTER_CONSUMER_SECRET=<<twitter consumer secret>>
  - TWITTER_V2_CLIENT_ID=<<twitter v2 client id>>
  - TWITTER_V2_CLIENT_SECRET=<<twitter v2 client secret>>
  - TWITTER_V2_CALLBACK_URL=<<twitter v2 callback url>>
- others variables
  - BOX_CLIENT_ID=<box client id>
  - BOX_CLIENT_SECRET=<<box client secret>>
  - DROPBOX_CLIENT_ID=<<dropbox client id>>
  - DROPBOX_CLIENT_SECRET=<<dropbox client secret>>
  - GOOGLE_CLIENT_ID=<<google client id>>
  - GOOGLE_CLIENT_SECRET=<<google client secret>>
- clowder related 
  - CLOWDER_BASE_URL=https://clowder.server.com/
  - CLOWDER_GLOBAL_KEY=<<clowder global key>>
  - CLOWDER_ON=false (this will decide if SMILE use clowder or not)
Contact us the **[SRTI lab](https://srtilab.techservices.illinois.edu/about/)** if you have any question: <a href="mailto:srti-lab@illinois.edu">srti-lab@illinois.edu</a>
