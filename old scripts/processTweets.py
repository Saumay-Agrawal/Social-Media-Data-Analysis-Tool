from pymongo import MongoClient
import json
from pprint import pprint

client = MongoClient()
db = client["Tweets"]
delhi_collection = db["Delhi"]
delhi_tweets = delhi_collection.find()
# for tweet in delhi_tweets:
#     pprint(tweet)

db2 = client["dv-pbl-data"]

tshort = db2['tweetShort']
# tcontent = db['tweet-content']
# tcount = db['tweet-count']
for tweet in delhi_tweets:
    ts = {
        'created_at' : tweet['created_at'],
        'id' : tweet['id'],
        'text' : tweet['text'],
        'source' : tweet['source'],
        'user' : {
            'id' : tweet['user']['id'],
            'name' : tweet['user']['name'],
            'screen_name' : tweet['user']['screen_name'],
            'location' : tweet['user']['location'],
            'followers_count' : tweet['user']['followers_count'],
            'friends_count' : tweet['user']['friends_count'],
            'favourites_count' : tweet['user']['favourites_count'],
        }
    }
    tshort.insert(ts)
