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

def check(id_name):
    #id=copy.copy(n)

    start=datetime(2019,8,10,0,0)

    soldout=['完売','なくな','無くな','おわり','売り切れ','終了','終わり']

    newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended')
    for twt in newlist:
        nowid=twt.id
        if(twt.created_at>start):
            try:
                if(any((j in twt.full_text) for j in soldout)):
                    api.retweet(twt.id)
            except:
                pass
