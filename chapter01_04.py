# Chapter 01 크롤링과 웹 기본
# chapter 01-4 패턴으로 실습하며 익히기: HTML/CSS 이해를 바탕으로 크롤링하기
# 2019-12-11 22:10

import requests
from bs4 import BeautifulSoup
import lxml

res = requests.get('https://www.daum.net/')
soup = BeautifulSoup(res.content, "html.parser")

mydata = soup.find_all('a', attrs={'class':'link_issue', 'tabindex':'-1'})
for item in mydata:
    print(item.get_text())