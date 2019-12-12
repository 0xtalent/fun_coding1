# Chapter 01 크롤링과 웹 기본
# chapter 01-7 바로 실전 크롤링 해보기: 네이버 쇼핑 사이트 크롤링 하기
# 2019-12-12 09:36

import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, "html.parser")

data = soup.select('#popular_srch_lst > li > span.txt > a')
for item in data:
    print(item.get_text())

print()

res2 = requests.get('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000')
soup2 = BeautifulSoup(res2.content, "html.parser")

data2 = soup2.select('#productListArea > ul > li > p > a')
for item2 in data2:
    print(item2.get_text())
