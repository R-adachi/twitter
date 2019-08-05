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

def get():
    c96_list=[[]]

    f = open("../myname.txt", "r")
    myname = f.read()
    f.close()

    screen_name=myname #リスト作成者の@~~の~~
    listname="c96" #リストの名前
    for member in tweepy.Cursor(api.list_members,slug=listname,owner_screen_name=screen_name).items():
        c96_list.append([member.name,member.screen_name])

    del c96_list[0]

    return(c96_list)
