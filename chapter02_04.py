# Chapter 02 다양한 크롤링 기술과 업무 자동화 활용
# chapter 02-4 실전 크롤링과 강력한 크롤링 기술 팁4: 로그인이 필요한 웹피이지 크롤링을 위한 쿠키/세션 요청 찾기
# 2019-12-13 09:08

'''
1. 로그인할 때, ID/PW 넣고, 요청
2. 서버에서 ID/PW가 맞는지 확인하고, 이에 맞는 세션값을 응답헤더에 넣어서 전송
3. 웹브라우저가 해당 응답헤더에서 세션값을 찾아서, 이후에 해당 사이트 요청시에는 세션값을 함께 전송
4. 서버에서 해당 세션값에 맞는 ID를 확인하고, 해당 ID에 맞는 웹페이지를 응답바디에 넣어서 전송
5. 웹브라우저가 해당 웹페이지를 보여줌
'''