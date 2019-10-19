# GTHL standings scraper

## Usage

The data from scraping the site is pushed to firestore to be consumed later, for now only one league and tier is being scraped, and more may be added in the future.

## Deployment

Docker Image: https://hub.docker.com/r/nakamin/gthl-scraper
This project is deployed on gcp, and there is a cloudbuild pipeline setup that will:
1. On push to any GitHub branch, build the docker image and push to dockerhub
2. Restart the gcp compute vm to pull in the latest docker image
