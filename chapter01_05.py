# Chapter 01 크롤링과 웹 기본
# chapter 01-5 패턴으로 실습하며 익히기: CSS selector 사용해서 크롤링하기
# 2019-12-12 08:50

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, "html.parser")

data = soup.select('h3.tit_view')
print(data)

# 셀렉트는 리스트로 가져온다, 클래스가 두개 일때 . 으로 연결
# find는 find_all 일때만 리스트로 가져온다.
# copy selector 로 가져오면 됨