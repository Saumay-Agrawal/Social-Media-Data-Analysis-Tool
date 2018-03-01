
import tweepy
import json
from pymongo import MongoClient

# declaring API tokens and keys
consumer_key = 'j1FlUU9B8VqWuJOSndGNy97sH'
consumer_secret = 'O9qCrVNGt6MbMAmvMDxYJulZrRv4IP0hAxWqGAm0CMydNdIBDA'
access_token = '3187334840-TPM1J1kiuhKP6ZQe2ozDCPHTaSOoJvA6y3nF2VS'
access_token_secret = 'HuyUzZRG6o30JGnk7QOPmW3jo0q57qbgIS67CJWpA8ITe'

# Establishing connection with twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Establishing connection with mongodb
client = MongoClient()
db = client["TwitterData"]

# delhi_collection = db["Delhi"]
# delhi_cursor = tweepy.Cursor(api.search,q="#MyRightToBreathe OR #CropBurning OR #Smog OR #DelhiPollution OR #DelhiAirPollution OR #DelhiSmog",count=100)
# delhi_count = 1
# for tweet in delhi_cursor.items(limit=10000):
#     delhi_collection.insert(tweet._json)
#     print("processed tweet #", delhi_count)
#     delhi_count+=1

# mumbai_collection = db["Mumbai"]
# mumbai_cursor = tweepy.Cursor(api.search,q="#MumbaiRains OR #CycloneOckhi",count=100)
# mumbai_count = 1
# for tweet in mumbai_cursor.items(limit=10000):
#     mumbai_collection.insert(tweet._json)
#     print("processed tweet #", mumbai_count)
#     mumbai_count+=1

# print('Tweets from mumbai: ', mumbai_count)
# print('Tweets from delhi: ', delhi_count)

def getHomeTimeline():
    collection = db['HomeTimeline']
    tweets = api.home_timeline()
    count = 0
    for tweet in tweets:
        collection.insert(tweet._json)
        count += 1
    print(count, 'tweets stored in the database.')

trends = api.trends_available()

