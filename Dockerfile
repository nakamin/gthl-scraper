# find out how to authenticate firebase from gcp vm
# make item pipeline to push to firebase
FROM python:3
WORKDIR /usr/local/bin/gthl-scraper
# install google chrome and cron
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get -y update \
    && apt-get install -y google-chrome-stable cron
# install chromedriver
RUN apt-get install -yqq unzip \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
# set display port to avoid crash
ENV DISPLAY=:99
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
# add cron job to run scraper job daily
RUN echo "@daily cd /usr/local/bin/gthl-scraper && scrapy crawl teams" > /etc/cron.d/scrapybot
ENTRYPOINT [ "cron", "-f" ]
