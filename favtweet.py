#!/usr/bin/env python
# twitter/bots/favtweet.py

import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def favtweet(api):
    tweets = api.home_timeline(count=1)
    tweet = tweets[0]

    logger.info(f"Processing tweet id {tweet.id} of {tweet.author.name}")
    for tweet in tweets:
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)


def main():
    api = create_api()
    while True:
        favtweet(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
