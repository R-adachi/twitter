from pprint import pprint
import get_ill_list_module as getillist
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic
import time
import key_module as getkey
import tweepy

def make(makelist_name,member):
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

    if makelist_name not in api.lists_all(screen_name=myname):
        api.create_list(name=makelist_name,mode="private")

    for l in member:
        api.add_list_member(screen_name=l, slug=makelist_name, owner_screen_name=myname)
