#!/bin/bash
CONTAINER_DIR="/home/sambedeau/tweepy-bots/"
echo "-----------------------------------------------"
echo "building container"
sudo docker build -t fave-retweet-bot ${CONTAINER_DIR}
