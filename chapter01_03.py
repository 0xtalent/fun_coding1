# Chapter 01 크롤링과 웹 기본
# chapter 01-3 패턴으로 실습하며 익히기: HTML/CSS 이해를 바탕으로 크롤링하기
# 2019-12-11 21:49

import requests
from bs4 import BeautifulSoup
import lxml

# css 언어 적용하기
# 1. 적용할 태그에 style 속성으로 넣기
# 2. HTML 문서 <head> 안에 <style> 태그로 넣기
# 3. 문서 <head> 안에 CSS 파일로 링크하기

# html에서 class가 css인 거 처음 알았네ㅋㅋ 개념이 부족하니까 쫌 흔들렸구나
# 잔재미 코딩으로 제대로 시작해보자, 빠르게

res = requests.get('https://news.v.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, "html.parser")

mydata = soup.find('h3', 'tit_view')
print(mydata.get_text())
print()

mydata2 = soup.find_all('span', 'txt_info')
for item in mydata2:
    print(item.get_text())
print()

mydata3 = soup.find('div', 'layer_util layer_summary')
print(mydata3.get_text())

# 크롤링 후처리: \n, 불필요한 데이터 삭제, 깔끔하게 문자열 정리