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

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get(id_name):
    #id=copy.copy(n)

    start=datetime(2019,11,1,(17 - 9),0)

    nowid=0
    tourakuflg=0

    newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,retweeted=False,include_rts=False,tweet_mode='extended')
    #nowpage+=1
    for twt in newlist:
        nowid=twt.id
        if(twt.created_at>start):
            try:
                trtw=dp.seikei(twt.full_text)
                if(len(trtw)>3):
                    stop=1
                    api.retweet(twt.id)
                    tourakuflg=1
                else:
                    stop=0
            except:
                pass
            if(stop):
                time.sleep(30)



    for p in range(8):
        getlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,retweeted=False,include_rts=False,tweet_mode='extended',max_id=nowid)
        for twt in newlist:
            nowid=twt.id
            if(twt.created_at>start):
                try:
                    trtw=dp.seikei(twt.full_text)
                    if(len(trtw)>3):
                        stop=1
                        api.retweet(twt.id)
                        tourakuflg=1
                    else:
                        stop=0
                except:
                    pass
                if(stop):
                    time.sleep(30)
    return(tourakuflg)
#return
