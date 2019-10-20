# find out how to authenticate firebase from gcp vm
# make pipeline to push to firebase
# setup ci/cd pipeline with gcp
FROM selenium/standalone-chrome
WORKDIR /usr/local/bin/gthl-scraper
RUN sudo apt-get -y update && sudo apt-get -y install python3 python3-pip cron
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
# add cron job to run scraper job daily
RUN sudo echo "@daily cd /usr/local/bin/gthl-scraper && scrapy crawl teams" >/etc/cron.d/scrapybot
ENTRYPOINT [ "cron", "-f" ]
