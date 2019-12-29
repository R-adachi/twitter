import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os
import copy
import tempfile
import requests
import cv2
import c_judge_module as cnn
import shutil

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

start=datetime(2019,12,15,0,0)

osinaflg=False

sampleflg=False

osina=['お品','御品','おしな','お待ち']

sample=['表紙','サンプル','新刊','メロン','とら','通販']

nowid=0

day='2'

id_name='lemon_mito'

name='test'

p='test'

flg=0

newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended')
#nowpage+=1
for twt in newlist:
    nowid=twt.id
    if(twt.created_at>start):
        try:
            for i in twt.extended_entities['media']:
                #if(osina in twt.full_text):
                if(any((j in twt.full_text) for j in osina)):
                #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                    pic_dir=('../c97/pic/'+day+'/'+name+p+'/お品書き/')
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                flg=1
        except:
            pass
        if(flg):
                tmp_dir=('../tmp/')
                if not os.path.exists(tmp_dir):
                    os.makedirs(tmp_dir)
                tmp_path=os.path.join(tmp_dir, os.path.basename(i['media_url']))
                with urllib.request.urlopen(i['media_url']) as w:
                    data = w.read()
                    with open(tmp_path, mode='wb') as local_file:
                        local_file.write(data)
                print(tmp_path)
                img=cv2.imread(tmp_path)
                print(cnn.judge(img))
                # if(cnn.judge(img)):
                    # print('oshina')
                #pprint(i['media_url'])
                shutil.rmtree(tmp_dir)
