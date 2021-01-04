#!/usr/bin/env python
# tweepy-bots/bots/fav.py

import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self,tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # If tweet is a reply or i'm it's author, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logging.error("Error on fav and retweet",exc_info=True)
    def on_error(self, status):
        logger.error(status)

def main(keywords):
    api =create_api()
    tweets_listener = FavListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track =keywords, languages=["en"])

if __name__ == "__main__":
    main(["Mandalorian", "Star Wars"])
