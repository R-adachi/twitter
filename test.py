from pprint import pprint
import csv
import day_place_module as dp
from datetime import datetime
import tweepy
import key_module as getkey

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open("../myname.txt", "r")
myname = f.read()
f.close()

newlist = api.user_timeline(screen_name=myname,count=200,exclude_replies=False,include_rts=True,tweet_mode='extended')

start=datetime(2019,11,1,(17 - 9),10)

for twt in newlist:
    if(twt.created_at>start):
        dp.seikei_comp(twt.full_text)
