# Chapter 01 크롤링과 웹 기본
# chapter 01-10 크롤링을 위한 지식: 꼭 알아둬야 할 데이터 포멧 - JSON 포맷 이해하기
# 2019-12-12 15:03

import json

# 네이버 뉴스에서, android 라는 키워드로 검색한 결과
data = """
{
    "lastBuildDate": "Thu, 12 Dec 2019 14:40:52 +0900",
    "total": 20930,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "&quot;삼성, 내년 2월 '노이즈 캔슬링' 기능 넣은 갤럭시 버즈 플러스 출시한다&quot;",
            "originallink": "https://www.insight.co.kr/news/258804",
            "link": "https://www.insight.co.kr/news/258804",
            "description": "애플의 에어팟 플러스와 비슷한 클래스라고 보면 된다.삼성전자 무선이어폰 '갤럭시 버즈' / <b>Android</b> Central 삼성전자는 내년 2월 갤럭시S11 시리즈를 공식 발표할 때 이 갤럭시 버즈 플러스도 함께 공개할 계획으로... ",
            "pubDate": "Thu, 12 Dec 2019 13:58:00 +0900"
        },
        {
            "title": "HMD글로벌, 저가형 안드로이드 고 스마트폰 '노키아 C1' 공개",
            "originallink": "http://kbench.com/?q=node/205760",
            "link": "http://kbench.com/?q=node/205760",
            "description": "핀란드 스마트폰 스타트업 HMD 글로벌에서 신흥 시장 공략을 위해 안드로이드 고 에디션(<b>Android</b> Go Edition) 스마트폰 '노키아 C1'을 공개했다. 노키아 C1은 480 x 960 픽셀 해상도의 5.45인치 디스플레이를... ",
            "pubDate": "Thu, 12 Dec 2019 10:14:00 +0900"
        },
        {
            "title": "'갤럭시노트10' 안드로이드 10 정식 업데이트 임박? 5차 업데이트 출시",
            "originallink": "http://kbench.com/?q=node/205755",
            "link": "http://kbench.com/?q=node/205755",
            "description": "이번 업데이트에서는 ▲카메라 메모리 누수 현상 ▲구독 캘린더 설정 중 가로모드 전환하면 FC발생 ▲<b>android</b>.process.media 등 일부 안드로이드 프로세스 어플리케이션들이 지속적으로 다운됨 ▲클립보드 엣지 표시... ",
            "pubDate": "Thu, 12 Dec 2019 09:56:00 +0900"
        },
        {
            "title": "스카이스캐너, ‘여행 트렌드 2020’ 보고서 통해 가성비 여행지 공개",
            "originallink": "http://www.tourtimes.net/147255",
            "link": "http://www.tourtimes.net/147255",
            "description": "스카이스캐너는 컴퓨터, 모바일에서 사용할 수 있으며, 앱(<b>Android</b>/iOS)은 1억 만번의 다운로드를 기록했다. 스카이스캐너의 목표는 1200여 여행 파트너들과 협력하여, 현대적이고 지속 가능한 여행으로 세계적인 변화를... ",
            "pubDate": "Thu, 12 Dec 2019 09:28:00 +0900"
        },
        {
            "title": "마이크론, 읽기 속도 최대 1050MB/s 휴대용 SSD 크루셜 X8 출시",
            "originallink": "http://www.epnc.co.kr/news/articleView.html?idxno=92984",
            "link": "http://www.epnc.co.kr/news/articleView.html?idxno=92984",
            "description": "PC, Mac, PS4, XBOX One, iPad Pro, Chromebook, USB 3.2 Gen2 인터페이스를 사용하는 일부 <b>Android</b> 장치 등 다양한 장치와 호환되며, 최대 7.5ft(2.3m) 높이의 낙하 충격을 견뎌낸다. 사용자는 사진, 동영상, 문서, 음악을... ",
            "pubDate": "Thu, 12 Dec 2019 09:10:00 +0900"
        },
        {
            "title": "A Student Who Makes African Emojis",
            "originallink": "https://www.nytimes.com/2019/12/11/style/a-student-who-makes-african-emojis.html?partner=naver",
            "link": "https://www.nytimes.com/2019/12/11/style/a-student-who-makes-african-emojis.html?partner=naver",
            "description": "The emojis, which he calls Zouzoukwa (which translates roughly as “image” in the regional Bété language), have been downloaded on more than 120,000 <b>Android</b> phones and iPhones since their... ",
            "pubDate": "Thu, 12 Dec 2019 07:00:00 +0900"
        },
        {
            "title": "Review: A Multimedia Excavation of Lispector’s ‘Wild Heart’",
            "originallink": "https://www.nytimes.com/2019/12/11/theater/near-to-the-wild-heart-review-lispector.html?partner=naver",
            "link": "https://www.nytimes.com/2019/12/11/theater/near-to-the-wild-heart-review-lispector.html?partner=naver",
            "description": "A female <b>android</b> looking at its hands in puzzlement is projected against a starry sky when Joana feels most detached, while a ghostly apparition (Lisa Giobbi) sleepwalks in the background when... ",
            "pubDate": "Thu, 12 Dec 2019 02:10:00 +0900"
        },
        {
            "title": "[민간기업 일자리 정보+] NCS직업교육협회, 사단법인 전통문화연구회, 이평중...",
            "originallink": "http://www.fintechpost.co.kr/news/articleView.html?idxno=94730",
            "link": "http://www.fintechpost.co.kr/news/articleView.html?idxno=94730",
            "description": "▲ 채용회사명 : (주)탑앤스카우트, 채용공고명 : &quot;[업계 1위 골프솔루션] Native (iOS / <b>Android</b>) 앱개발자 충원&quot;, 담당업무 : 응용 프로그래밍, 본사 또는 근무지 : 서울 강남구, 고용형태 : 정규직, 지원자격 : 경력3~15년|학력무관... ",
            "pubDate": "Thu, 12 Dec 2019 00:58:00 +0900"
        },
        {
            "title": "생활의 필수품 '스마트폰' 분실 했다면?…앱으로 분실된 스마트폰 위치 확인 ...",
            "originallink": "http://famtimes.co.kr/news/view/494059",
            "link": "http://famtimes.co.kr/news/view/494059",
            "description": "'나의 스마트폰 찾기 어플' 활용안드로이드를 기반으로 한 스마트폰의 경우에는 '<b>Android</b> 기기 관리자' 링크를 눌러 웹페이지에 접속해 핸드폰에 연결시킨 구글 계정을 활용하면 위치추적이 가능해 분실된 핸드폰의 위치를... ",
            "pubDate": "Thu, 12 Dec 2019 00:04:00 +0900"
        },
        {
            "title": "Gift Ideas for Car Lovers or Commuters",
            "originallink": "https://www.nytimes.com/2019/12/11/business/car-gifts.html?partner=naver",
            "link": "https://www.nytimes.com/2019/12/11/business/car-gifts.html?partner=naver",
            "description": "For those topping the nice list, try an audio system upgrade to add wireless <b>Android</b> Auto or... It starts with ID cars that pair to <b>Android</b> and iOS devices with a free app. Stored in a “digital... ",
            "pubDate": "Wed, 11 Dec 2019 20:02:00 +0900"
        }
    ]
}
"""

json_data = json.loads(data)

print(json_data['items'][0]['title'])