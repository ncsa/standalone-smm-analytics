FROM socialmediamacroscope/autophrase:base 

# overwrite
WORKDIR /AutoPhrase
COPY . ./
ENV RABBITMQ_HOST="rabbitmq"

# set environmet variables to prevent interactive prompt duing installation of openjdk
ENV DEBIAN_FRONTEND=noninteractive
ENV REGION=US
ENV TZ=America/Chicago

# install dependency libraries
RUN apt-get -y update \
&& apt-get -y install g++ openjdk-8-jdk curl python3-pip \
&& pip3 install -r requirement.txt \
# switch work directory to be AutoPhrase
&& /bin/bash -c "source compile.sh" \
# cron job clean tmp folder
&& chmod u+x ./clear_cache.sh \
&& chmod 0644 ./clear_cache_cron \
&& crontab ./clear_cache_cron
