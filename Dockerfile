FROM selenium/standalone-chrome
WORKDIR /usr/local/bin/gthl-scraper
USER root
RUN apt-get update && apt-get install -y python3-pip
USER seluser
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT [ "scrapy", "crawl", "table" ]
