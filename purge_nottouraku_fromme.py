import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy
import day_place_module as dp
import time

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#id=copy.copy(n)

f = open("../myname.txt", "r")
myname = f.read()
f.close()

start=datetime(2019,11,1,(17 - 9),0)

nowid=0
tourakuflg=0

newlist = api.user_timeline(screen_name=myname,count=200,exclude_replies=False,include_rts=True,tweet_mode='extended')
#nowpage+=1
stop=0
for twt in newlist:
    nowid=twt.id
    if(twt.created_at>start):
        trtw=dp.seikei(twt.full_text)
        #print(twt.full_text)
        if(len(trtw)==0):
            status = api.get_status(twt.id, include_my_retweet=1)
            if status.retweeted == True:
                api.unretweet(twt.id)
                stop=1
            else:
                stop=0
    if(stop):
        time.sleep(0)
    stop=0
stop=0
for p in range(8):
    print(p)
    getlist = api.user_timeline(screen_name=myname,count=200,exclude_replies=False,include_rts=True,tweet_mode='extended',max_id=nowid)
    for twt in newlist:
        nowid=twt.id
        if(twt.created_at>start):
            try:
                trtw=dp.seikei(twt.full_text)
                if(len(trtw)==0):
                    stop=1
                    status = api.get_status(twt.id, include_my_retweet=1)
                    if status.retweeted == True:
                        api.unretweet(twt.id)
                        stop=1
                    else:
                        stop=0
            except:
                pass
        if(stop):
            time.sleep(0)
        stop=0
