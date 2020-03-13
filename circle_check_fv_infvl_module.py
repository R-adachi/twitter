import tweepy
import key_module as getkey
from pprint import pprint
import csv
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

stop=0

def check(id_name):
    #id=copy.copy(n)

    start = schedule.touraku_schedule()

    nowid=0

    newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,favorited=False,retweeted=False,include_rts=False,tweet_mode='extended')
    #newlist = api.list_timeline(owner=myname, slug[, since_id][, max_id][, per_page][, page])
    for twt in newlist:
        #print(twt.created_at)
        nowid=twt.id
        if(twt.created_at>start):
            try:
                trtw=touraku.touraku(twt.full_text)
                if(len(trtw)>3):
                    trtw.insert(0, twt.user.screen_name)
                    #print(twt.user.screen_name)
                    stop=1
                    api.create_favorite(twt.id)
                else:
                    stop=0
            except:
                pass
            if(stop):
                time.sleep(30)

    for p in range(8):
        newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,favorited=False,retweeted=False,include_rts=False,tweet_mode='extended',max_id=nowid)
        #newlist = api.list_timeline(owner=myname, slug[, since_id][, max_id][, per_page][, page])
        for twt in newlist:
            #print(twt.created_at)
            nowid=twt.id
            if(twt.created_at>start):
                try:
                    trtw=touraku.touraku(twt.full_text)
                    if(len(trtw)>3):
                        trtw.insert(0, twt.user.screen_name)
                        #print(twt.user.screen_name)
                        stop=1
                        rtlist.append(trtw)
                        api.create_favorite(twt.id)
                        #api.retweet(twt.id)
                    else:
                        stop=0
                except:
                    pass
                if(stop):
                    time.sleep(30)
