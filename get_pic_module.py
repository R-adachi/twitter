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

def get(id_name,name,day,p):

    dir=('../pic/'+day+'/'+name+'_'+p+'/')
    if not os.path.exists(dir):
        os.makedirs(dir)
    #id=copy.copy(n)

    start=datetime(2019,12,15,0,0)

    osinaflg=False

    sampleflg=False

    osinaflg2=False

    osina=['お品','御品','おしな','お待ち']

    sample=['表紙','サンプル','新刊','メロン','とら','通販']

    nowid=0

    newlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended')
    #nowpage+=1
    for twt in newlist:
        osinaflg2=False
        nowid=twt.id
        if(twt.created_at>start):
            try:
                for i in twt.extended_entities['media']:
                    #if(osina in twt.full_text):
                    if(any((j in twt.full_text) for j in osina)):
                    #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                        pic_dir=('../pic/'+day+'/'+name+'_'+p+'/お品書き/')
                        if not os.path.exists(pic_dir):
                            os.makedirs(pic_dir)
                        pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                        with urllib.request.urlopen(i['media_url']) as w:
                            data = w.read()
                            with open(pic_path, mode='wb') as local_file:
                                local_file.write(data)
                        osinaflg=True
                    elif(any((j in twt.full_text) for j in sample)):
                    #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                        pic_dir=('../pic/'+day+'/'+name+'_'+p+'/サンプル/')
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
                        tmp_dir=('../tmp/')
                        if not os.path.exists(tmp_dir):
                            os.makedirs(tmp_dir)
                        tmp_path=os.path.join(tmp_dir, os.path.basename(i['media_url']))
                        with urllib.request.urlopen(i['media_url']) as w:
                            data = w.read()
                            with open(tmp_path, mode='wb') as local_file:
                                local_file.write(data)
                        img=cv2.imread(tmp_path)
                        if(cnn.judge(img)):
                            osinaflg2=True
                            osinaflg=True
                            print('osina')
                        else:
                            print('not osina')
                        shutil.rmtree(tmp_dir)

                        pic_dir=('../pic/'+day+'/'+name+'_'+p)
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
            if(osinaflg2):
                for i in twt.extended_entities['media']:
                    #if(osina in twt.full_text):
                    pic_dir=('../pic/'+day+'/'+name+'_'+p+'/お品書き/')
                    if not os.path.exists(pic_dir):
                        os.makedirs(pic_dir)
                    pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                    with urllib.request.urlopen(i['media_url']) as w:
                        data = w.read()
                        with open(pic_path, mode='wb') as local_file:
                            local_file.write(data)
                osinaflg2=False


    for p in range(8):
        getlist = api.user_timeline(screen_name=id_name,count=200,exclude_replies=True,include_rts=False,tweet_mode='extended',max_id=nowid)
        for twt in getlist:
            osinaflg2=False
            nowid=twt.id
            if(twt.created_at>start):
                try:
                    for i in twt.extended_entities['media']:
                        #if(osina in twt.full_text):
                        if(any((j in twt.full_text) for j in osina)):
                        #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                            pic_dir=('../pic/'+day+'/'+name+'_'+p+'/お品書き/')
                            if not os.path.exists(pic_dir):
                                os.makedirs(pic_dir)
                            pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                            with urllib.request.urlopen(i['media_url']) as w:
                                data = w.read()
                                with open(pic_path, mode='wb') as local_file:
                                    local_file.write(data)
                            osinaflg=True
                        elif(any((j in twt.full_text) for j in sample)):
                        #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                            pic_dir=('../pic/'+day+'/'+name+'_'+p+'/サンプル/')
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
                            tmp_dir=('../tmp/')
                            if not os.path.exists(tmp_dir):
                                os.makedirs(tmp_dir)
                            tmp_path=os.path.join(tmp_dir, os.path.basename(i['media_url']))
                            with urllib.request.urlopen(i['media_url']) as w:
                                data = w.read()
                                with open(tmp_path, mode='wb') as local_file:
                                    local_file.write(data)
                            img=cv2.imread(tmp_path)
                            if(cnn.judge(img)):
                                osinaflg2=True
                                osinaflg=True
                                print('osina')
                            else:
                                print('not osina')
                            shutil.rmtree(tmp_dir)

                            pic_dir=('../pic/'+day+'/'+name+'_'+p)
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
                if(osinaflg2):
                    for i in twt.extended_entities['media']:
                        #if(osina in twt.full_text):
                        if(any((j in twt.full_text) for j in osina)):
                        #if(('おしながき' in twt.full_text) or ('お品書き' in twt.full_text)):
                            pic_dir=('../pic/'+day+'/'+name+p+'/お品書き/')
                            if not os.path.exists(pic_dir):
                                os.makedirs(pic_dir)
                            pic_path=os.path.join(pic_dir, os.path.basename(i['media_url']))
                            with urllib.request.urlopen(i['media_url']) as w:
                                data = w.read()
                                with open(pic_path, mode='wb') as local_file:
                                    local_file.write(data)
                    osinaflg2=False
    return(osinaflg)
#return
