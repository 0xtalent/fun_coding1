# Chapter 01 크롤링과 웹 기본
# chapter 01-1 패턴으로 실습하며 익히기: 크롤링 코드 패턴으로 익히기
# 2019-12-10 20:34

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20170615203441266')
print(res.content)