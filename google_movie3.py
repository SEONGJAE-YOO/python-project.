from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기
# 모니터(해상도) 높이인 1440 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1440)") # 2560 X 1440
# browser.execute_script("window.scrollTo(0, 2880)") # 2560 X 1440

# 화면 가장 아래로 스크롤 내리기 
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") #현재 문서의 높이만큼 스크롤 내린다.

# browser.execute_script("window.scrollTo(0,1080") #내 노트북 해상도 1920 * 1080 
#1080 위치로 스크롤 내리기
import time
interval = 4 # 4초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollheght")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollheght")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
    # 활인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "활인되지 않은 영화 제외")
        continue

    # 활인된 가격
    price = movie.find("span", attrs={"class", "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # "https://play.google.com" + link

    print(f"제목 : {title}")
    print(f"할인 전 가격 : {original_price}")
    print(f"할인 후 가격 : {price}")
    print("링크 : " + "https://play.google.com" + link)
    print("-" * 100)

browser.quit()


'''
#실행결과
DevTools listening on ws://127.0.0.1:50426/devtools/browser/b801a123-c347-4075-a2a7-b51736b9ae9c
스크롤 완료
110
담보
날씨의 아이 (자막)
해리포터와 마법사의 돌
뮬란
기생충
너의 이름은. (자막판)
애프터 : 그 후
해리포터와 비밀의방
어벤져스 : 엔드게임 (자막판)
아웃포스트
스파이더맨 : 뉴 유니버스
오케이 마담
반도
해리포터와 아즈카반의 죄수 (자막판)
베놈   Venom
국제수사
건마의 신:어린 아내의 알바
겨울왕국 2 (자막판)
겨울왕국 2 (더빙판)
금지된 섹스, 달콤한 복수
조커
해리포터와 불의잔
기기괴괴 성형수
제목 : 기기괴괴 성형수
할인 전 가격 : ₩10,000
할인 후 가격 : ₩7,000
링크 : https://play.google.com/store/movies/details/%EA%B8%B0%EA%B8%B0%EA%B4%B4%EA%B4%B4_%EC%84%B1%ED%98%95%EC%88%98?id=BJHacR8HVys.P
----------------------------------------------------------------------------------------------------
스파이더맨: 파 프롬 홈 (자막판)
소리도없이
해리포터와 불사조 기사단
날씨의 아이 (더빙)
다만악에서구하소서
해리포터와 혼혈왕자
1917
목소리의 형태 (자막판)
슈퍼 소닉
해리포터와 죽음의 성물 파트 2 (자막판)
레디 플레이어 원
해리포터와 죽음의 성물 파트1 (자막판)
팀버튼의 크리스마스 악몽
코코 (자막판)
위대한 쇼맨 (자막판)
50가지 그림자:해방 (자막판)
성판17: 남자들의 17가지 성적 판타지
해리포터 시리즈 완결 패키지
존윅 3: 파라벨룸
분노의 질주: 홉스 & 쇼
언힌지드
나쁜 녀석들 : 포에버 Bad Boys for Life
코코 (더빙판)
스타 이즈 본
슈퍼배드 3 (더빙판)
50가지 그림자: 심연
강철비2: 정상회담 확장판
몬스터 호텔 3 (더빙판)
미드웨이
트롤 :월드투어
스파이더맨: 홈커밍  (자막판)
에이바
제목 : 에이바
할인 전 가격 : ₩10,000
할인 후 가격 : ₩4,500
링크 : https://play.google.com/store/movies/details/%EC%97%90%EC%9D%B4%EB%B0%94?id=8OReSr6sYUU.P
----------------------------------------------------------------------------------------------------
라라랜드 (자막판)
콰이어트 플레이스 (자막판)
포드 V 페라리 (자막판)
너의 이름은. (더빙판)
보헤미안 랩소디 (자막판)
엽문4 더 파이널
아쿠아맨
해리포터와 아즈카반의 죄수 (더빙판)
쥬라기 월드 : 폴른 킹덤 (자막판)
나쁜 녀석들:더 무비
그레이의 50가지 그림자
명탐정 피카츄 (더빙판)
존 윅-리로드
핵소고지 (자막판)
유령신부
알리타: 배틀 엔젤 (자막판)
인터스텔라
분노의 질주: 더 익스트림
부산행
AK-47
메이즈 러너: 데스 큐어 (자막판)
어벤져스 : 엔드게임 (더빙판)
애프터
나이브스 아웃
죽지않는 인간들의 밤
마이펫의 이중생활 2
악인전
제목 : 악인전
할인 전 가격 : ₩2,500
할인 후 가격 : ₩1,200
링크 : https://play.google.com/store/movies/details/%EC%95%85%EC%9D%B8%EC%A0%84?id=UCEcCDOv3r4.P
----------------------------------------------------------------------------------------------------
아바타
어벤져스 : 인피니티 워 (자막판)
극한직업
뮬란_중국판
드래곤 길들이기 3 (더빙판)
덩케르크 (자막판)
주토피아 (더빙판)
알라딘 (2019) (자막판)
쥬라기 월드
신비한 동물들과 그린델왈드의 범죄
에스파트너
인셉션
레옹 디 오리지널 (자막판)
어바웃 타임
블러드샷
할로윈 (자막판)
위플래쉬
인비저블맨
터미네이터: 다크 페이트
쿵푸팬더 3 (더빙판)
시간을 달리는 소녀_자막 (자막판)
천국의 셋방 (무삭제)
겟아웃 (자막판)
스폰지밥 (더빙판)
모아나 (더빙판)
강철비2 정상회담
제목 : 강철비2 정상회담
할인 전 가격 : ₩7,000
할인 후 가격 : ₩5,000
링크 : https://play.google.com/store/movies/details/%EA%B0%95%EC%B2%A0%EB%B9%842_%EC%A0%95%EC%83%81%ED%9A%8C%EB%8B%B4?id=EiNJ9TtZ68Q.P
----------------------------------------------------------------------------------------------------
오!문희
소스 코드
'''