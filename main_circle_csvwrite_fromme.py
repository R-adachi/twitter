from pprint import pprint
import csv
import day_place_module as dp
from datetime import datetime
import tweepy
import key_module as getkey
import get_csv_module as getcsv

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

circle_name=getcsv.get_c96_set()
name_list=getcsv.get()

f = open("../myname.txt", "r")
myname = f.read()
f.close()

kekka_list=[]

newlist = api.user_timeline(screen_name=myname,count=200,exclude_replies=True,include_rts=True,retweeted=True,tweet_mode='extended')
start=datetime(2019,11,1,(17 - 9),10)

for twt in newlist:
    try:
        if(twt.created_at>start):
            trtw=dp.seikei_comp(twt.full_text)
            moto_screen_name=twt.retweeted_status.user.screen_name
            if(len(trtw)>0):
                if(moto_screen_name in name_list):
                    nameset=circle_name[name_list.index(moto_screen_name)]
                    kekka_list.append([nameset[0],nameset[1],moto_screen_name,trtw])
                else:
                    kekka_list.append(['','',moto_screen_name,trtw])
    except:
        pass

with open('../c97.csv', 'w', encoding='shift_jis') as f:
    writer = csv.writer(f)
    writer.writerows(kekka_list)
