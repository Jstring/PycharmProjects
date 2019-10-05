import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


#크롤링 부분 + 페이징

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for pg in range(1,6):
    data = requests.get('https://genie.co.kr/chart/top200?ditc=D&ymd=20191006&hh=01&rtm=Y&pg=' + str(pg), headers = headers)


    soup = BeautifulSoup(data.text, 'html.parser')
    musics = soup.select('.list > .info')
# 몽고DB 저장 부분
    musicRank = 50*(pg-1)
    for music in musics:
        musicRank = musicRank +1
        musicTitle = music.select_one('.title').text
        musicArtist = music.select_one('.artist').text

        db.genieChart.insert_one({'rank': musicRank, 'title': musicTitle, 'artist': musicArtist})





