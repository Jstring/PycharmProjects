
# //크롤링 테스트
# import requests # requests 라이브러리 설치 필요
# from bs4 import BeautifulSoup
#
# import requests
# from bs4 import BeautifulSoup
#
# # 타겟 URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)
#
# # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
# soup = BeautifulSoup(data.text, 'html.parser')
#
# movies = soup.select('#old_content > table > tbody > tr')
# print(movies)




# // 파이썬 api get 연습
# def get_idex_mvl(gu_name):
#     r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#     rjson = r.json()['RealtimeCityAir']['row']
#
#     # for i in range(rjson['RealtimeCityAir']['list_total_count']):
#     # -> 파이썬은 for문에서 인덱스 아니라 리스트 인자를 그대로 가져옴
#     for rjson in rjson:
#         if rjson['MSRSTE_NM'] == gu_name:
#             if rjson['IDEX_NM'] == '보통':
#                 return print(gu_name, "의 미세먼지는 " , rjson['IDEX_MVL'], "입니다.")
#             else :
#                 return print('미세먼지 측정에 문제가 있습니다.')
#
# get_idex_mvl('중구')
# get_idex_mvl('서초구')
# get_idex_mvl('강남구')
#
