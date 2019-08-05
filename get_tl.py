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

status_list = api.home_timeline(count=200,include_rts=False)

tl=[]

pprint(status_list[0])

for i in status_list:
    tl.append([i.text])

#pprint(status_list[0].text)
#pprint(status_list)

with open('../mytl.csv', 'w' ,encoding="utf_8_sig") as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(tl)     # list（1次元配列）の場合
