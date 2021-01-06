#!/bin/bash
CONTAINER_DIR="/home/sambedeau/tweepy-bots/"
# Fill in authentication variables with own generated api keys
echo "-------------------------------------------"
echo "running container from image"
sudo docker run -it -e CONSUMER_KEY="" -e CONSUMER_SECRET="" -e ACCESS_TOKEN="" -e ACCESS_TOKEN_SECRET="" fave-retweet-bot
