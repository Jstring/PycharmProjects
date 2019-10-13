from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

import requests
from bs4 import BeautifulSoup

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/post', methods=['GET'])
def listing():
    # 클라이언트로부터 데이터를 받는 부분
    author_receive = request.args.get('author_give')

    # mongoDB에서 불러오는 부분
    if author_receive is not None:
        result = list(db.urls.find({"author": author_receive}, {'_id': 0}))
    else:
        result = list(db.urls.find({}, {'_id': 0}))


    # articles라는 키 값으로 영화정보 내려주기

    return jsonify({'result':'success', 'articles':result})


@app.route('/saveArticle', methods=['POST'])
def saving():
    # 클라이언트로붵 데이터를 받는 부분

    #fancy한 벨리데이션 체크
    required_fields = ['url_give', 'author_give', 'comment_give']
    for required_field in required_fields:
        if required_field not in request.form:
            return jsonify({'result': 'fail', 'msg': '{}값이 없습니다.'.format(required_field)})

    # if 'url_give' not in request.form:
    #     return jsonify({'result': 'fail', 'info': 'url값이 없습니다'})
    # if 'author_give' not in request.form:
    #     return jsonify({'result': 'fail', 'info': 'author값이 없습니다'})
    # if 'comment_give' not in request.form:
    #     return jsonify({'result': 'fail', 'info': 'comment 값이 없습니다'})

    url_receive = request.form['url_give']
    author_receive = request.form['author_give']
    comment_receive = request.form['comment_give']


    # meta tag를 스크래핑 하는 부분

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_image = soup.select_one('meta[property="og:image"]')['content']
    og_description = soup.select_one('meta[property="og:description"]')['content']

    # DB에 저장하는 부분
    data = {'url' : url_receive, 'author': author_receive, 'comment': comment_receive, 'title':og_title, 'image':og_image, 'desc':og_description}
    db.urls.insert(data)
    info = db.urls.find_one({'url' : url_receive},{'_id': 0})

    return jsonify({'result': 'success', 'info': info})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)