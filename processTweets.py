from pymongo import MongoClient
import json
from pprint import pprint

client = MongoClient()
db = client["Tweets"]

mumbai_collection = db["Mumbai"]
mumbai_tweets = mumbai_collection.find()
for tweet in mumbai_tweets:
    pprint(tweet)

delhi_collection = db["Delhi"]
delhi_tweets = delhi_collection.find()
for tweet in delhi_tweets:
    pprint(tweet)
