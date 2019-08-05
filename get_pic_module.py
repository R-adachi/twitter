import tweepy
import key_module as getkey
from pprint import pprint
import csv
from datetime import datetime
import urllib.error
import urllib.request
import os

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

name='Lownine'

start=datetime(2019,7,25,0,0)

getlist = api.user_timeline(screen_name=name,count=100,include_rts=False,tweet_mode='extended')

osina=False

for twt in getlist:
    if(twt.created_at>start):
        try:
            for i in twt.extended_entities['media']:
                if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                    pic_dir=('../pic/'+name+'/お品書き/')
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                    #pprint(i['media_url'])
                    osina=True
                else:
                    pic_dir=('../pic/'+name)
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                    #pprint(i['media_url'])
        except:
            pass
