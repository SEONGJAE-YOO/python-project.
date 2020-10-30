from bs4 import BeautifulSoup
from urllib.request import urlopen
 
url = 'https://comic.naver.com/webtoon/weekday.nhn'     # 웹툰 페이지 주소
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')   # url에 해당하는 페이지의 HTML 태그를 저장한다.
 
soup = soup.find_all('a', 'title')          # a태그에 title속성을 가지고 있는 HTML 태그들을 filtering하여 저장한다.
 
for each in soup :
    print(each.attrs['title'])              # title 속성값을 출력한다
    
#실행결과
'''
그녀의 버킷리스트
인싸라이프
신이 담긴 아이
소녀 해미
무주의 맹시
오늘도 사랑하세요
Here U Are
여름은 뜨겁다
위험한 신입사원
죽여주는 탐정님
불발소년
선녀야 야옹해봐!
#너무 길어서 생략합니다
'''

'''
# 2번째 방법
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# class : "title"인 모든 엘리먼트를 찾자
# find는 그 조건에 해당되는 첫번째 엘리먼트만 찾음
# find_all은 조건에 해당되는 모든 엘리먼트 찾음
cartoons = soup.find_all("a",attrs={"class":"title"})
for cartoon in cartoons : 
    print(cartoon.get_text())
'''