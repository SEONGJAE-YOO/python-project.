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
interval = 2 # 4초에 한번씩 스크롤 내림

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

    # 활인된 가격  /<span class="VfPpfd ZdBevf i5DZme"><span>₩7,000</span></span>
    price = movie.find("span", attrs={"class", "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 /<a href="/store/movies/details/%EA%B2%A8%EC%9A%B8%EC%99%95%EA%B5%AD_2_%EC%9E%90%EB%A7%89%ED%8C%90?id=9kTBYkw3zH8" aria-hidden="true" tabindex="-1" class="JC71ub"></a>
    link = movie.find("a", attrs={"class":"JC71ub"})["href"] #모든 영화 포스터 링크들이 클래스가 "JC71ub"이다
    # "https://play.google.com" + link

    print(f"제목 : {title}")
    print(f"할인 전 가격 : {original_price}")
    print(f"할인 후 가격 : {price}")
    print("링크 : " + "https://play.google.com" + link)
    print("-" * 100)

browser.quit()


'''   
#실행결과
DevTools listening on ws://127.0.0.1:50555/devtools/browser/2918b488-6920-4ffa-86f8-c0d7885e4ba4
스크롤 완료
110
검객
담보
날씨의 아이 (자막)
해리포터와 마법사의 돌
뮬란
스파이더맨 : 뉴 유니버스
기생충
겨울왕국 2 (자막판)
너의 이름은. (자막판)
베놈   Venom
해리포터와 비밀의방
반도
어벤져스 : 엔드게임 (자막판)
겨울왕국 2 (더빙판)
건마의 신:어린 아내의 알바
해리포터와 아즈카반의 죄수 (자막판)
오케이 마담
아웃포스트
애프터 : 그 후
스파이더맨: 파 프롬 홈 (자막판)
국제수사
금지된 섹스, 달콤한 복수
해리포터와 불의잔
소리도없이
조커
해리포터와 불사조 기사단
해리포터와 혼혈왕자
목소리의 형태 (자막판)
해리포터와 죽음의 성물 파트 2 (자막판)
슈퍼 소닉
해리포터와 죽음의 성물 파트1 (자막판)
레디 플레이어 원
1917
스타 이즈 본
위대한 쇼맨 (자막판)
날씨의 아이 (더빙)
기기괴괴 성형수
제목 : 기기괴괴 성형수
할인 전 가격 : ₩10,000
할인 후 가격 : ₩7,000
링크 : https://play.google.com/store/movies/details/%EA%B8%B0%EA%B8%B0%EA%B4%B4%EA%B4%B4_%EC%84%B1%ED%98%95%EC%88%98?id=BJHacR8HVys.P
----------------------------------------------------------------------------------------------------
포드 V 페라리 (자막판)
다만악에서구하소서
라라랜드 (자막판)
나쁜 녀석들 : 포에버 Bad Boys for Life
분노의 질주: 홉스 & 쇼
존윅 3: 파라벨룸
해리포터 시리즈 완결 패키지
50가지 그림자:해방 (자막판)
성판17: 남자들의 17가지 성적 판타지
코코 (자막판)
그레이의 50가지 그림자
스파이더맨: 홈커밍  (자막판)
핵소고지 (자막판)
존 윅-리로드
슈퍼배드 3 (더빙판)
세이프
트롤 :월드투어
쥬라기 월드 : 폴른 킹덤 (자막판)
언힌지드
몬스터 호텔 3 (더빙판)
아쿠아맨
50가지 그림자: 심연
에스파트너
마이펫의 이중생활 2
엽문4 더 파이널
강철비2: 정상회담 확장판
명탐정 피카츄 (더빙판)
인터스텔라
알라딘 (2019) (자막판)
슈퍼 소닉
팀버튼의 크리스마스 악몽
쿵푸팬더 3 (더빙판)
메이즈 러너: 데스 큐어 (자막판)
에이바
제목 : 에이바
할인 전 가격 : ₩10,000
할인 후 가격 : ₩4,500
링크 : https://play.google.com/store/movies/details/%EC%97%90%EC%9D%B4%EB%B0%94?id=8OReSr6sYUU.P
----------------------------------------------------------------------------------------------------
악인전
제목 : 악인전
할인 전 가격 : ₩2,500
할인 후 가격 : ₩1,200
링크 : https://play.google.com/store/movies/details/%EC%95%85%EC%9D%B8%EC%A0%84?id=UCEcCDOv3r4.P
----------------------------------------------------------------------------------------------------
어벤져스 : 인피니티 워 (자막판)
미드웨이
아바타
부산행
나이브스 아웃
쥬라기 월드
애프터
너의 이름은. (더빙판)
덩케르크 (자막판)
나쁜 녀석들:더 무비
나 홀로 집에 (자막판)
드래곤 길들이기 3 (더빙판)
코코 (더빙판)
극한직업
해리포터와 아즈카반의 죄수 (더빙판)
분노의 질주: 더 익스트림
블러드샷
비긴 어게인 (자막판)
알리타: 배틀 엔젤 (자막판)
레미제라블
보헤미안 랩소디 (자막판)
AK-47
씽 (더빙판)
어벤져스 (자막판)
헝거게임: 더 파이널
캡틴 아메리카 : 시빌 워 (자막판)
터미네이터: 다크 페이트
주토피아 (더빙판)
위플래쉬
천국의 셋방 (무삭제)
죽지않는 인간들의 밤
인셉션
어바웃 타임
겟아웃 (자막판)
콰이어트 플레이스 (자막판)
토르 : 라그나로크 (자막판)
온워드: 단 하루의 기적
신비한 동물들과 그린델왈드의 범죄
'''