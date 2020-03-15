from pprint import pprint
import time
from progressbar import progressbar as pber
from requests_oauthlib import OAuth1Session
import key_module as getkey
import schedule_crawler_module as schedule
from datetime import datetime

consumer_key = getkey.get_ckey()
consumer_secret = getkey.get_ckey_s()
access_token = getkey.get_atoken()
access_token_secret = getkey.get_atoken_s()

twitter = OAuth1Session(consumer_key,consumer_secret,access_token,access_token_secret)

url = "https://api.twitter.com/1.1/favorites/list.json"

delfv_url = "https://api.twitter.com/1.1/favorites/destroy.json"

f = open("../myname.txt", "r")
myname = f.read()
f.close()

nowid = 0

time = schedule.touraku_schedule()

params={'screen_name' : myname, 'count' : 200, 'tweet_mode' : 'extended'}

response = twitter.get(url, params = params)

newlist=response.json()

for twt in pber(newlist):
    nowid = twt['id']
    twttime = twt['created_at'].split(' ')
    del twttime[4]
    if(datetime.strptime(' '.join(twttime),'%a %b %d %H:%M:%S %Y')>time):
        if(twt['retweeted']):
            delfv_params={'id' : twt['id']}
            twitter.post(delfv_url,delfv_params)

for i in range(8):
    params={'screen_name' : myname, 'count' : 200, 'tweet_mode' : 'extended', 'max_id' : nowid}

    response = twitter.get(url, params = params)

    newlist=response.json()

    for twt in pber(newlist):
        nowid = twt['id']
        twttime = twt['created_at'].split(' ')
        del twttime[4]
        if(datetime.strptime(' '.join(twttime),'%a %b %d %H:%M:%S %Y')>time):
            if(twt['retweeted']):
                delfv_params={'id' : twt['id']}
                twitter.post(delfv_url,delfv_params)
