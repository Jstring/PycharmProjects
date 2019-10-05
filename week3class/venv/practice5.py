import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

url = 'https://ppss.kr'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

articles = soup.select('article > a')
for article in articles:
    link = article['href']
    articleData = requests.get(link, headers = headers)
    articleSoup = BeautifulSoup(articleData.text, 'html.parser')
    ogImage = articleSoup.select_one('meta[property="og:image"]')['content']
    ogTitle = articleSoup.select_one('meta[property="og:title"]')['content']
    ogDescription = articleSoup.select_one('meta[property="og:description"]')['content']

    db.urls.insert_one({'og:image':ogImage, 'og:title':ogTitle, 'og:description':ogDescription})








# og:image
# og: title
# og: description