#!/usr/bin/env python
import tweepy
from config import create_api

# Authenticate to Twitter with both public and secret keys
# Remove keys when publishing to Git

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Prints out the latest 20 entries in your timeline
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
# Posts a tweet
#api.update_status("Test tweet from another place -_+")

# Retrieve user details
# NOTE: randomUser is not an actual user, change for test purposes
user = api.get_user("randomUser")
print("User details:")
print(f"Name is: {user.name}, bio is: {user.description}, location is: {user.location}")
print ("Last 20 Followers")
for people in user.followers():
    print(people.name)


