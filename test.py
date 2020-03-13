import tweepy
import key_module as getkey
from pprint import pprint
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy
import kobun_touraku_module as touraku
import time
import schedule_crawler_module as schedule

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

newlist = api.user_timeline(myname,slug='cells_comp',count=1,exclude_replies=True,retweeted=False,include_rts=False,tweet_mode='extended')
#newlist = api.list_timeline(owner=myname, slug[, since_id][, max_id][, per_page][, page])
for twt in newlist:
    print(twt.full_text)
