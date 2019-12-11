# Chapter 01 크롤링과 웹 기본
# chapter 01-2 패턴으로 실습하며 익히기: HTML 이해를 바탕으로 크롤링하기
# 2019-12-11 21:09

import requests
from bs4 import BeautifulSoup
import lxml

# HTML은 마크업 언어(문서와 데이터의 구조를 표현하는 언어)입니다.

res = requests.get('https://news.v.daum.net/v/20190620110108639')
# print(res.content)
soup = BeautifulSoup(res.content, "html.parser")

mydata = soup.find('h3')
print(mydata.get_text())

# 따옴표 3개로 문자열로 넣거나
# \ 역슬래시로 구분해주면
# 여러 줄에 걸쳐 있어도 오류 안남

# 여러가지로 할 수 있다.

# data = soup.find('p', class_='cssstyle')
# data = soup.find('p', 'cssstyle')
# data = soup.find('p', attrs={'class':'cssstyle'})
# data = soup.find('p', 'id':'body', 'align':'center')