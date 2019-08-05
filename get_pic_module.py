import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.request

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name='GirlsFrontline'

start=datetime(2019,7,25,0,0)

getlist = api.user_timeline(screen_name=name,count=200,include_rts=False,tweet_mode='extended')

for twt in getlist:
    if(twt.created_at>start):
        try:
            for i in twt.extended_entities['media']:
                pprint(i['media_url'])
            #pprint(twt.extended_entities['media'])
            print(twt.full_text)
        except:
            pass
