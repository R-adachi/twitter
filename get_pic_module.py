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

def get(id_name,name):
    #id=copy.copy(n)

    start=datetime(2019,7,25,0,0)

    osinaflg=False

    sampleflg=False

    osina=['お品','御品','おしな','お待ち']

    sample=['表紙','サンプル','新刊','メロン','とら','通販']

    nowid=0

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
                    elif(any((j in twt.full_text) for j in sample)):
                    #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                        pic_dir=('../pic/'+name+'/サンプル/')
                        if not os.path.exists(pic_dir):
                            os.makedirs(pic_dir)
                        pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                        with urllib.request.urlopen(i['media_url']) as w:
                            data = w.read()
                            with open(pic_path, mode='wb') as local_file:
                                local_file.write(data)
                        #pprint(i['media_url'])
                        sampleflg=True
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
                #pprint(twt.full_text)


    for p in range(8):
        getlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended',max_id=nowid)
        for twt in getlist:
            nowid=twt.id
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
                        elif(any((j in twt.full_text) for j in sample)):
                        #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                            pic_dir=('../pic/'+name+'/サンプル/')
                            if not os.path.exists(pic_dir):
                                os.makedirs(pic_dir)
                            pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                            with urllib.request.urlopen(i['media_url']) as w:
                                data = w.read()
                                with open(pic_path, mode='wb') as local_file:
                                    local_file.write(data)
                            #pprint(i['media_url'])
                            sampleflg=True
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
                    #pprint(twt.full_text)
    return(osinaflg)
#return
