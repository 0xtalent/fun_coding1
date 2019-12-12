# Chapter 01 크롤링과 웹 기본
# chapter 01-5 패턴으로 실습하며 익히기: CSS selector 사용해서 크롤링하기2
# 2019-12-12 09:36

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.naver.com')
soup = BeautifulSoup(res.content, "html.parser")

data = soup.select('div.ah_roll.PM_CL_realtimeKeyword_rolling_base')
for item in data:
    print(item.get_text().strip())

print()

res2 = requests.get('https://news.v.daum.net/v/20170615203441266')
soup2 = BeautifulSoup(res2.content, "html.parser")

data2 = soup2.select('html head title')
for item2 in data2:
    print(item2.get_text())