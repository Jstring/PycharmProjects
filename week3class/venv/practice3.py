# 엑셀에 저장
# import requests
# from bs4 import BeautifulSoup
# from openpyxl import load_workbook
#
# work_book = load_workbook('prac01.xlsx')
# work_sheet = work_book['prac']
#
# work_sheet.cell(row=1, column=1, value='rank')
# work_sheet.cell(row=1, column=1, value='title')
# work_sheet.cell(row=1, column=1, value='star')
#
# # URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')
#
# # movies (tr들) 의 반복문을 돌리기
# rank = 1
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if not a_tag == None:
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#
#         work_sheet.cell(row=rank+1, column=1, value=rank)
#         work_sheet.cell(row=rank + 1, column=2, value=title)
#         work_sheet.cell(row=rank + 1, column=3, value=star)
#         rank += 1
#
#
#
# work_book.save('prac01.xlsx')
#

# 몽고디비에 저장

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다


# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
# rank = 1
# for movie in movies:
#     # movie 안에 a 가 있으면,
#     a_tag = movie.select_one('td.title > div > a')
#     if not a_tag == None:
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#
#         db.movies.insert_one({'rank': rank, 'title':title, 'star':star})
#         rank += 1
#

star = db.movies.find_one({'title': '사운드 오브 뮤직'}, {'_id':0})

lists = list(db.movies.find({'star': star['star']}))

for list in lists:
    print(list['title'])


db.movies.update_many({'star': star['star']},{ '$set': {'star':0} })

for list in lists:
    print(list['rank'])
