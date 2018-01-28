import tweepy
import json
from pymongo import MongoClient

consumer_key = 'j1FlUU9B8VqWuJOSndGNy97sH'
consumer_secret = 'O9qCrVNGt6MbMAmvMDxYJulZrRv4IP0hAxWqGAm0CMydNdIBDA'
access_token = '3187334840-TPM1J1kiuhKP6ZQe2ozDCPHTaSOoJvA6y3nF2VS'
access_token_secret = 'HuyUzZRG6o30JGnk7QOPmW3jo0q57qbgIS67CJWpA8ITe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# data = '['
# delhi_cursor = tweepy.Cursor(api.search,q="#MyRightToBreathe OR #CropBurning OR #Smog OR #DelhiPollution OR #DelhiAirPollution OR #DelhiSmog")
# delhi_count = 1
# file = open('delhi.json', mode='w', encoding='utf-8')
# file.write('[')
# for tweet in delhi_cursor.items():
#     file.write(json.dumps(tweet._json, sort_keys=True))
#     file.write(',')
#     data += json.dumps(tweet._json, sort_keys=True) + ','
#     print('processed tweet #', delhi_count)
#     delhi_count+=1
#     # if delhi_count == 100:
#     #     break
# file.write(']')
# # data = data[:-1] + ']'
# # file.write(data)
# file.close()

# print('tweet count: ', delhi_count)
# mumbai_cursor = tweepy.Cursor(api.search,q="#MumbaiRains OR #CycloneOckhi",count=100)
# mumbai_count = 1
# for tweet in mumbai_cursor.items(limit=10000):
#     print(json.dumps(tweet._json))
#     print("processed tweet #", mumbai_count)
#     mumbai_count+=1

data = '['
ny_cursor = tweepy.Cursor(api.search,q="#NewYear2018")
ny_count = 1
file = open('ny2018.json', mode='w', encoding='utf-8')
file.write('[')
for tweet in ny_cursor.items():
    file.write(json.dumps(tweet._json, sort_keys=True))
    file.write(',')
    data += json.dumps(tweet._json, sort_keys=True) + ','
    print('processed tweet #', ny_count)
    ny_count+=1
    # if delhi_count == 100:
    #     break
file.write(']')
# data = data[:-1] + ']'
# file.write(data)
file.close()

