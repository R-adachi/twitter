from pprint import pprint
import get_ill_list_module as getillist
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic
import time
import key_module as getkey
import tweepy

alist=getcsv.getoverA()
unlist=getcsv.getUn()
illist=getillist.get()

alist.extend(illist)
list=list(set(alist))

blist=getcsv.getB()
clist=getcsv.getC()
blist.extend(clist)

for r in blist:
    try:
        list.remove(r)
    except:
        pass

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

try:
    api.create_list(name="c97_pre",mode="private")
except:
    pass
"""
for l in list:
    api.add_list_member("c97_pre", id=l)
"""
