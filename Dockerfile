FROM python:3-alpine
WORKDIR /usr/local/bin/gthl-scraper
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apk update && apk add --no-cache chromium-chromedriver
COPY ./scraper ./scraper
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./settings_docker.py ./scraper/settings.py
ENTRYPOINT [ "scrapy", "crawl", "table" ]