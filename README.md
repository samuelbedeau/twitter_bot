# Tweepy API twitter_bot containerised with Docker
The following repo uses Tweepy: an open source Python package which abstracts a lot of complexity away in accessing Twitter API with Python. 

The python scripts are then containerised and are made an image, then run in an container which packages all code and its dependencies so it can virtually run on anything and anywhere regardless of OS restraints/versions, etc. 

## Getting Started
First of all you will need: 
1. Virtual environment for your scripts
2. Docker installed on your workstation
3. API keys generated by Twitter API 

A lot of the instructions below will be on the assumption that you have Docker installed, and have basic-to-intermediate python knowledge so you should be aware of how to install a virtual environment, REST APIs, etc.

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
#### Authentication
Authentication will be API keys. You have the consumer key and consumer secret key, as well as access token and access secret token.

```
import tweepy

consumer_key = ""
consumer_secret_key = ""
access_token = ""
access_token_secret = ""
```
Once you have supplied your keys, you can create a Tweepy authentication object and assign the object's tokens then verify the credentials
```
auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
try:
    api.verify_credentials()
```
Once this is done and verify_credentials returns true, you are good to go with playing around with Tweepy's methods and testing the twitter api.

### Tweepy fundamentals
To start displaying tweets, liking them or retweeting them, we are going to have to retrieve these tweets.
This is done by creating a StreamListener.

```
import tweepy

class Listener(tweepy.StreamListener):
    
    def on_status(self,status):
        print(status.text)
```
Then you can create a Stream which will work hand in hand with the listener to retrieve tweets.
```
myListener = Listener()
myStream = tweepy.Stream(api.auth, myListener)
```

## Docker 
To run these scripts in an image we are going to have to create a Dockerfile
The base image will be python, then we will copy in the scripts, any dependencies via pip (where the requirements.txt file comes in)
and have a starting command

After that we'll build the image

And run it in a container. 
Here will be a condensed version of the dockerfile just to lay out an example
``` 
FROM python:3.7-alpine
```
This is your base image command. So what the image pulls from. It can be anything from a java image, to even an image that you have built before too. Python is our base image because
our container is for one purpose only: Python scripts. 

Containers are meant to be lightweight so it won't have everything like a VM would have running on it.

```
COPY bots/fav.py /bots/
```
Next we have a copy instruction which is where we copy in our files into what will be the container's shell/ file directory
Once you have run the container you can actually jump into the container's shell and see these files if you pull an 'ls' command
```
RUN pip install -r /tmp/requirements.txt
```
This is to install dependencies, imports for the scripts you just copied in. 
```
WORKDIR /bots
```
This command sets the working directory of your Docker container. Every command will be executed from the specified directory

```
CMD ["python3", "fav.py"]
```
This the command that is executed by default when the container runs. In this case we will be executing the fav.py script.

### Building and Running
To build your Dockerfile into an image you would run a command like this: 
```
(tweepVenvenv) hostname:~/tweepy-bots$ sudo docker build . -t fav-retweet-bot
```
Then to run the image:
```
sudo docker run -it -e CONSUMER_KEY="" -e CONSUMER_SECRET="" -e ACCESS_TOKEN="" -e ACCESS_TOKEN_SECRET="" fave-retweet-bot
```
Once you have set these up, feel free to check Tweepy documentation and my repo to play around with the api!
Happy Python'ing and Docker'ing!
