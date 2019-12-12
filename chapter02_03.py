# Chapter 02 다양한 크롤링 기술과 업무 자동화 활용
# chapter 02-3 크롤링과 업무 자동화 기술: 네이버 Open API 활용, 네이버쇼핑 엑셀 보고서 만들기
# 2019-12-12 19:12

import requests
import openpyxl

client_id = '1Rppd33QXGoeY2_Hl0e4'
client_secret = '6oFwGgU792'

start, num = 1, 0

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 100
excel_sheet.append(['랭킹', '제목', '링크'])

for index in range(10):
    start_number = start + (index * 100)
    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start={}'.format(start_number)
    header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    # print(naver_open_api)

    res = requests.get(naver_open_api, headers=header_params)

    if res.status_code == 200:
        data = res.json()
        for item in data['items']:
            num += 1
            excel_sheet.append([num, item['title'], item['link']])
    else:
        print("Error Code", res.status_code)

excel_file.save('shopping.xlsx')
excel_file.close()