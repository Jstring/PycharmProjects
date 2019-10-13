from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    # 클라이언트로부터 데이터를 받는 부분
    item_receive = request.args.get('item_give')

    # mongoDB에서 불러오는 부분
    if item_receive is not None:
        result = list(db.orders.find({"item": item_receive}, {'_id': 0}))
    else:
        result = list(db.orders.find({}, {'_id': 0}))

    # orders 키 값으로 영화정보 내려주기

    return jsonify({'result':'success', 'orders':result})


@app.route('/order', methods=['POST'])
def makeOrder():
    #벨리데이션 체크
    required_fields = ['name_give', 'count_give', 'address_give', 'phone_give', 'item_give']
    for required_field in required_fields:
        if required_field not in request.form or request.form[required_field] == "":
            return jsonify({'result': 'fail', 'msg': '{}값이 없습니다.'.format(required_field)})

    item_receive = request.form['item_give']
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    # DB에 저장하는 부분
    data = {'item' : item_receive, 'name': name_receive, 'count': count_receive , 'address': address_receive , 'phone': phone_receive}
    db.orders.insert(data)
    info = db.orders.find_one({'name' : name_receive},{'_id': 0})

    return jsonify({'result': 'success', 'info': info})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)