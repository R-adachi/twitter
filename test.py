import tweepy
import key_module as getkey
from pprint import pprint
import csv
import datetime

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#status_list = api.home_timeline()


#c96_list=[[]]
def get(listname):
    list=[]

    f = open("../myname.txt", "r")
    myname = f.read()
    f.close()

    screen_name=myname #リスト作成者の@~~の~~
    for member in tweepy.Cursor(api.list_members,slug=listname,owner_screen_name=screen_name).items():
        #c96_list.append([member.screen_name])
        list.append(member.screen_name)
    pprint(datetime.datetime.fromtimestamp(api.rate_limit_status()['resources']['lists']['/lists/members']['reset']))
    #del c96_list[0]
    #pprint(status_list[0].text)
    #pprint(status_list)

    return(list)

if __name__=='__main__':
    list=get('c98rt')
    #print(list)
