#!/usr/bin/python

import tweepy
from pymongo import MongoClient
import time
import datetime
import os
 
client = MongoClient( "mongodb", 27017)
db = client.twitter
collection = db["twitter"]

consumer_key = '3hnURtSKcJihqQINPuoAzEGDk'
consumer_secret = 'YByJQj6e1Vmm3YszzKtscOMQEwLzPGONqhANko1yi6YngawOkp'
access_token = '3186303628-JG8xdBpC5q2QkJnuj7uw4MYFDWGFvCqCU9phGY4'
access_token_secret = 'lyDjJhQ1VKMv0aabgX9Wn3Efr2Tf0Ag1xk1a9BVg6hm2f'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.search,q="#laundering OR #money OR #security OR #iot", lang="en").items(10):
   print (tweet.created_at, tweet.text)
   record = {
        'created_at': tweet.created_at,
        'text': tweet.text
        }
   db.twitter.insert_one(record)

print("mongodb content")
data = collection.find()
for item in data:
  print(item["created_at"].strftime("%d/%m/%y %H:%M"),item["text"])
