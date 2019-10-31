from pprint import pprint
import get_ill_list_module as getillist
import get_csv_module as getcsv
import get_list_module as getlist
import csv
import get_pic_module as getpic
import time
import key_module as getkey
import tweepy
"""
alist=getcsv.getoverA()
unlist=getcsv.getUn()
illist=getillist.get()
"""
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

api.create_list(name="c97_pre",mode="private")

"""
kekka=[[]]

cnt=0

for i in clist:
    check=(i in llist)
    kekka.append([clist_name[cnt],i,check,daylist[cnt],plist[cnt]])
    cnt+=1

del kekka[0]

with open('../c97_prelist.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(kekka)
"""
