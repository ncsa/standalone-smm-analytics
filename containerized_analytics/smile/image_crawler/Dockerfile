FROM ubuntu:18.04

RUN mkdir -p /scripts

WORKDIR /scripts

# copy paste python scripts
COPY . ./

ENV RABBITMQ_HOST="rabbitmq"

# install dependency libraries
RUN apt-get update \
&& apt-get -y install python3-pip \
&& apt-get -y install cron \
# install dependency libraries and download required data
&& pip3 install -r requirement.txt \
# cron job clean tmp folder
&& chmod u+x ./clear_cache.sh \
&& chmod 0644 ./clear_cache_cron \
&& crontab ./clear_cache_cron