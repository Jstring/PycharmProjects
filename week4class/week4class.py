from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/movie', methods=['GET'])
def get_movie():
    # rank_give로 클라이언트가 준 rank을 가져오기
    if request.args.get('rank') is not None:
       rank_receive = request.args.get('rank')
       rank_receive = int(rank_receive)
       movie_info = db.movies.find_one({'rank': rank_receive}, {'_id': 0})
    elif request.args.get('title') is not None:
       title_receive = request.args.get('title')
       movie_info = db.movies.find_one({'title': title_receive}, {'_id': 0})

    # rank_receive를 숫자로 만들어주기 (db엔 숫자로 저장되어있으니까!)
    # rank의 값이 받은 rank와 일치하는 document 찾기 & _id 값은 출력에서 제외하기
    # info라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'info':movie_info})

@app.route('/movie', methods=['POST'])
def post_movie():
   rank_receive = request.form['rank']
   rank_receive = int(rank_receive)
   likes_receive = request.form['likes']

   db.movies.update_one({'rank': rank_receive}, {'$set': {'likes': likes_receive}})
   movie_info = db.movies.find_one({'rank': rank_receive}, {'_id': 0})
   return jsonify({'result': 'success', 'info': movie_info})

@app.route('/new', methods=['POST'])
def post_():

   if 'rank' not in request.form:
      return jsonify({'result': 'success', 'info': 'rank값이 없습니다'})
   if 'title' not in request.form:
      return jsonify({'result': 'success', 'info': 'rank값이 없습니다'})
   if 'rating' not in request.form:
      return jsonify({'result': 'success', 'info': 'rank값이 없습니다'})
   if 'likes' not in request.form:
      return jsonify({'result': 'success', 'info': 'rank값이 없습니다'})

   else:
      rank_receive = request.form['rank']
      title_receive = request.form['title']
      rating_receive = request.form['rating']
      likes_receive = request.form['likes']
      likes_receive = int(likes_receive)
      rank_receive = int(rank_receive)
      rating_receive = float(rating_receive)

      if db.movies.find_one({'rank': rank_receive}) is None:
         db.movies.insert_one({'rank': rank_receive, 'title': title_receive, 'star': rating_receive, 'likes':likes_receive})


      else:
         db.movies.update({'rank': rank_receive}, {'$set': {'title': title_receive, 'star':rating_receive, 'likes':likes_receive}})

      movie_info = db.movies.find_one({'rank': rank_receive}, {'_id': 0})
      return jsonify({'result': 'success', 'info': movie_info})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)