# Chapter 01 크롤링과 웹 기본
# chapter 01-9 패턴으로 실습하며 익히기: urllib 라이브러리 사용법
# 2019-12-12 11:28

import requests
from bs4 import BeautifulSoup
import lxml

res = requests.get('https://seeko.earlyadopter.co.kr/bbs/board.php?bo_table=mainnews')
soup = BeautifulSoup(res.content, "lxml")

data = soup.select('#fboardlist > div.list-board > ul > li')
for item in data:
    print(item.get_text())

# 쩝 urllib로 했는데 잘 안되서, requests로 했는데, 후처리가 잘 안되네
# 지금은 여기까지 밖에 못함. 더 공부하면 될 듯^^



