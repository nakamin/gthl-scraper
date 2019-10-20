# find out how to authenticate firebase from gcp vm
# make pipeline to push to firebase
FROM selenium/standalone-chrome
USER root
WORKDIR /usr/local/bin/gthl-scraper
RUN apt-get -y update && apt-get -y install python3 python3-pip cron
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
# add cron job to run scraper job daily
RUN echo "@daily cd /usr/local/bin/gthl-scraper && scrapy crawl teams" > /etc/cron.d/scrapybot
ENTRYPOINT [ "cron", "-f" ]
