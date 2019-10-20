# find out how to authenticate firebase from gcp vm
# make item pipeline to push to firebase
FROM ubuntu
WORKDIR /usr/local/bin/gthl-scraper
RUN apt-get install -yqq unzip cron python3 python3-pip wget \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get -y update \
    && apt-get install -y google-chrome-stable
ENV DISPLAY=:99
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
RUN echo "@daily cd /usr/local/bin/gthl-scraper && scrapy crawl teams" > /etc/cron.d/scrapybot
ENTRYPOINT [ "cron", "-f" ]
