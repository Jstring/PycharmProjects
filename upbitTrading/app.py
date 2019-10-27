from flask import Flask, render_template, jsonify, request, Response

app = Flask(__name__)

import json
import requests
import pprint

# html렌더
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/list', methods=["POST"])
def refreshList() :


   url = "https://api.upbit.com/v1/market/all"

   responses = requests.request("GET", url)
   jsonResponses = json.loads(responses.text) # ??결과값이 text인데 json형식으로 바꿔줘야함. 여기서 한참막힘ㅠㅠ : 항상 해줘야하는 과정
   krw = "KRW-"

   db.coinList.delete_many({}) # ?? 다 지우지 않고 데이터의 최신을 유지하는 방법 궁금
   coinNum = 1
   for response in jsonResponses:
      if response['market'].find(krw) != -1:
         coinMarket = response['market']
         coinName = response['english_name']

         data = {'coinNum':coinNum , 'coinName': coinName, 'coinMarket': coinMarket}
         db.coinList.insert_one(data)

         coinNum = coinNum + 1

         # print(response['market'])
   lists = list(db.coinList.find({},{'coinMarket': 1, '_id':0}))

   return jsonify({'result': 'success', 'data': lists }) #???? 리턴에서 뭘 줘야하지? 500에러를 안내고싶다. -> 줘야하는 값 주기



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)