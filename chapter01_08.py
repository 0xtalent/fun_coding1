# Chapter 01 크롤링과 웹 기본
# chapter 01-8 바로 실전 크롤링 해보기: 네이버 주식 사이트 크롤링 하기
# 2019-12-12 11:14

import requests
from bs4 import BeautifulSoup

res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, "html.parser")

data = soup.select('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr > th')
for item in data:
    print(item.get_text())

# 크롤링 하고 다시 재 크롤링으로 후처리