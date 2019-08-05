import tweepy
import key_module as getkey
from pprint import pprint
import csv

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#status_list = api.home_timeline()


#c96_list=[[]]
def get(name):
    status_list = api.home_timeline(count=1000,include_rts=False)

    tl=[]

    pprint(status_list[0])

    for i in status_list:
        tl.append([i.text])
