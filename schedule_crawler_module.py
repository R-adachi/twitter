import requests
import json
import bs4
import datetime
import re
import jaconv

def touraku_schedule():
    url = "https://www.comiket.co.jp/cdbms/"

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    match = re.findall(r'\]\s+\[.+\]', soup.text)
    year = (match[0].replace('[', '').replace(']', '').split(' ')[5])

    before_str = ''
    for i in soup.select('font'):
        if(i.get_text().startswith('当落発表')):
            day_str = before_str.split(' ')[0]
            day_str = jaconv.z2h(day_str,digit=True,ascii=True)
            date = datetime.datetime.strptime(year+day_str, '%Y%m月%d日')
        before_str = i.get_text()

    return(date)

def comiket_schedule(c):

    url = 'https://www.comiket.co.jp/info-a/'+c+'/'+c+'info.html'

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    for i in soup.select('meta'):
        schedule_text = i.get('content')

    schedule_text = jaconv.z2h(schedule_text,digit=True,ascii=True)
    schedule = re.findall(r'\d+', schedule_text)
    schedule = list(map(int,schedule))
    start = datetime.datetime(schedule[0],schedule[1],schedule[2])
    end = datetime.datetime(schedule[0],schedule[3],schedule[4])
    return(start,end)
