FROM python:3.7

RUN apt-get -qq -y update && apt-get -qq -y install cron \
&& mkdir -p /scripts
WORKDIR /scripts

# copy paste python scripts
COPY . ./

ENV RABBITMQ_HOST="rabbitmq"

# install dependency libraries and download required data
RUN pip install --no-cache-dir -r requirement.txt \
&& python3 -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet \
&& python3 -m spacy download en_core_web_sm \
# cron job clean tmp folder
&& chmod u+x ./clear_cache.sh \
&& chmod 0644 ./clear_cache_cron \
&& crontab ./clear_cache_cron

# wordnet cannot unzip fix
RUN unzip /usr/local/share/nltk_data/corpora/wordnet.zip -d /usr/local/share/nltk_data/corpora
