import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

id_name='abu0705'

name='abu'


start=datetime(2019,7,25,0,0)

osinaflg=False

osina=['お品','御品','おしな']

num=0

nowpage=1

nowid=0

newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended')
#nowpage+=1
for twt in newlist:
    nowid=twt.id
    num+=1
    if(twt.created_at>start):
        try:
            for i in twt.extended_entities['media']:
                #if(osina in twt.full_text):
                if(any((j in twt.full_text) for j in osina)):
                #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                    pic_dir=('../pic/'+name+'/お品書き/')
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                    #pprint(i['media_url'])
                    osinaflg=True
                else:
                    pic_dir=('../pic/'+name)
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                    pprint(i['media_url'])
        except:
            pprint(twt.full_text)


for p in range(10):
    getlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended',max_id=nowid)
    #nowpage+=1
    for twt in getlist:
        nowid=twt.id
        num+=1
        if(twt.created_at>start):
            try:
                for i in twt.extended_entities['media']:
                    #if(osina in twt.full_text):
                    if(any((j in twt.full_text) for j in osina)):
                    #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                        pic_dir=('../pic/'+name+'/お品書き/')
                        if not os.path.exists(pic_dir):
                            os.makedirs(pic_dir)
                        pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                        with urllib.request.urlopen(i['media_url']) as w:
                            data = w.read()
                            with open(pic_path, mode='wb') as local_file:
                                local_file.write(data)
                        #pprint(i['media_url'])
                        osinaflg=True
                    else:
                        pic_dir=('../pic/'+name)
                        if not os.path.exists(pic_dir):
                            os.makedirs(pic_dir)
                        pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                        with urllib.request.urlopen(i['media_url']) as w:
                            data = w.read()
                            with open(pic_path, mode='wb') as local_file:
                                local_file.write(data)
                        pprint(i['media_url'])
            except:
                pprint(twt.full_text)
print(num)
