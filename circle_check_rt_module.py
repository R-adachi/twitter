import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy

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

def check(listname):
    #id=copy.copy(n)

    start=datetime(2019,11,1,(15 - 9),0)

    newlist = api.list_timeline(myname,slug=listname,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended')
    #newlist = api.list_timeline(owner=myname, slug[, since_id][, max_id][, per_page][, page])
    for twt in newlist:
        #print(twt.created_at)
        nowid=twt.id
        if(twt.created_at>start):
            print(twt.full_text)
            """
            try:
                if(any((j in twt.full_text) for j in soldout)):
                    api.retweet(twt.id)
            except:
                pass
            """
