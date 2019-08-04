import tweepy
import csv
from pprint import pprint

csv_file=open("../key/key.csv","r",encoding="ms932",errors="",newline="")
f=csv.reader(csv_file,delimiter=",",doublequote=True,lineterminator="¥r¥n",quotechar='"',skipinitialspace=True)

list=[]

for row in f:
    list.append(row[0])

consumer_key        = list[0]
consumer_secret     = list[1]
access_token        = list[2]
access_token_secret = list[3]


def get_ckey():
    return consumer_key

def get_ckey_s():
    return consumer_secret

def get_atoken():
    return access_token

def get_atoken_s():
    return access_token_secret
