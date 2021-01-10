# Tweepy API twitter_bot containerised with Docker
The following repo uses Tweepy: an open source Python package which abstracts a lot of complexity away in accessing Twitter API with Python. 
The python scripts are then containerised and are made an image, then run in an container which packages all code and its dependencies so it can virtually run on anything and anywhere regardless of OS restraints/versions, etc. 

## Getting Started
First of all you will need: 
1. Virtual environment for your scripts
2. Docker installed on your workstation
3. API keys generated by Twitter API 

A lot of the instructions below will be on the assumption that you have Docker installed, and have basic-to-intermediate python knowledge so you should be aware of how to install a virtual environment etc.

First things first, we need to sign up to a twitter developer account in order to use the api. It is fairly easy to sign up, just fill in the information in the link below:
<https://developer.twitter.com/en/apply-for-access>

After that is done, let's create a virtual environment 
```
mkdir tweepVenv && cd tweepVenv
python3 -m venv tweepVenvenv
source tweepVenvenv/bin/activate
```

And create a directory for your scripts.
```
mkdir tweepy-bot && cd tweepy-bot
```

After that is done, install the tweepy module using pip
```
pip install tweepy
pip freeze > requirements.txt
```

### API practice
The fundamentals of this RESTful api is:
1. Authentication - assign api keys to api object you create when instantiating tweepy.API
2. Methods - Know the libraries methods such as:
```
api.get_user("randomUser")
```
## Brief Example
```
import tweepy
import os

def create_api():
    consumer_key - os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret =os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API()
    try:
        api.verify_credentials()
    except Exception as e:
        raise e
    return api
```

This is the basic authentication and creating your api object. 
Then using certain methods you can create various operations:
```
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
```
