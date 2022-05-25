import os
import tweepy
from dotenv import load_dotenv
import pbd

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token,
    access_token_secret
)

api = tweepy.API(auth)
me=api.verify_credentials()

print(me)
pbd.set_trace()