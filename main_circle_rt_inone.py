from pprint import pprint
import get_csv_module_v2 as getcsv
import get_list_module as getlist
import csv
import get_touraku_inone_module as touraku
import time
import day_place_module as dp
import get_ill_list_module as getillist
import tweepy
import key_module as getkey

print('C?:'end="")
c = 'C'+input()

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

cnt=0
nlist=getcsv.get_pre_grade(c)
kekka_list=[]
clist=[]
memlist=[]

f = open("../myname.txt", "r")
myname = f.read()
f.close()

listname="c97pre" #リストの名前
for member in tweepy.Cursor(api.list_members,slug=listname,owner_screen_name=myname).items():
    memlist.append(str(member.screen_name))

for n in nlist:
    kekka=dp.seikei(n[1])
    if(len(kekka)>0):
        kekka_list.append([n[0],True])
        clist.append(n[0])

for m in memlist:
    if(m not in clist):
        print(m)
        if(touraku.get(m)):
            kekka_list.append([m,True])
        else:
            kekka_list.append([m,False])


with open('../c97_check.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(kekka_list)
