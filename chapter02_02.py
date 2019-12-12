# Chapter 02 다양한 크롤링 기술과 업무 자동화 활용
# chapter 02-2 패턴으로 실습하며 익히기: 네이버 Open API로 크롤링 하기
# 2019-12-12 18:58

import requests
import pprint

client_id = '1Rppd33QXGoeY2_Hl0e4'
client_secret = '6oFwGgU792'

naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=갤럭시노트10'
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}

res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    data = res.json()
    for index, item in enumerate(data['items']):
        print(index + 1, item['title'], item['link'])
else:
    print("Error Code", res.status_code)