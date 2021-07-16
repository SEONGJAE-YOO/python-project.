#pip install beautifulsoup4  터미널에서 설치해줌
#pip install lxml 터미널에서 설치해줌 
#lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It provides safe and convenient access to these libraries using the ElementTree API.

import requests
from bs4 import BeautifulSoup  

url= "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()   #url 문제있으면 종료하도록 설정함

soup = BeautifulSoup(res.text,"lxml")  # 가져온 html문서를 lxml파서를 통해 BeautifulSoup 객체로 만든것
print(soup.title) 
# 실행결과: <title>네이버 만화</title>
print(soup.title.get_text()) 
#실행결과: 네이버 만화, <title>빼고 가져온다
print(soup.a)
# 실행결과: <a href="#menu" onclick="document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"><span>메인 메뉴로 바로가기</span></a> /처음으로 발견되는 <a> element 결과 실행됨  
print(soup.a.attrs) 
#실행결과 : {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
# a element 속성 정보 반환
print(soup.a["href"])# 실행결과: #menu
                     # a element의 href 속성 값 정보를 출력
print(soup.find("a",attrs={"class":"Nbtn_upload"})) #soup 객체내에 있는 모든 내용중에서 처음으로 발견되는 a태그에 해당하는 class 속성이 'Nbtn_upload' 부분만 모두 찾아준다 
#실행결과 : <a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
rank1 = soup.find("li",attrs={"class":"rank01"}) 
print(rank1.a)
#실행결과 : <a href="/webtoon/detail.nhn?titleId=736989&amp;no=50" onclick="nclk_v2(event,'rnk*p.cont','736989','1')" title="더 복서-50화 감사">더 복서-50화 감사</a>
print(rank1.a.get_text()) # a태그 안에 글자만 출력한다
#더 복서-50화 감사
print(rank1.next_sibling.next_sibling) # 줄바꿈이 있기 때문에 next_sibling 두번 써준다
#실행결과:
# <li class="rank02">
# <a href="/webtoon/detail.nhn?titleId=570503&amp;no=327" onclick="nclk_v2(event,'rnk*p.cont','570503','2')" title="연애혁명-323. 마음의 저울">연애혁명-323. 마음의 저울</a>       
# <span class="rankBox">
# <img alt="변동없음" height="10" src="https://ssl.pstatic.net/static/comic/images/migration/common/arrow_no.gif" title="변동없음" width="7"/> 0


#                                 </span>
# </li>
rank1 = soup.find("li",attrs={"class":"rank01"}) 

rank2 = rank1.next_sibling.next_sibling  #다음 <li> 클래스인 rank02를 가져온다
rank3 = rank2.next_sibling.next_sibling  #다음 <li> 클래스인 rank03를 가져온다
print(rank3.a.get_text()) #rank3 클래스인 <li>에서 글자만 출력해준다   
#실행결과:
#독립일기-39화 아침을 건강하게

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())
#실행결과
#연애혁명-323. 마음의 저울
print(rank1.parent) # rank1 클래스의 부모인 <ol class> ~ </ol> 의 정보들이 다 출력된다.
#실행결과 
#너무 길어서 생략합니다. 간단하게 설명하자면 <li class="rank1"> ~ <li class="rank10"> 까지 html 코드가 다 출력됨
rank2 = rank1.find_next_sibling("li") #rank1 클래스의 다음 정보인 <li>만 출력하도록 함 , rank2 = rank1.next_sibling.next_sibling 를 간단하게 만든 것
print(rank2.a.get_text())
#실행결과
#더 복서-50화 감사
# 방금전까지만 해도 rank2가 연예혁명이였는데 몇분안에 연예혁명이 1위가 되고  더 복서가 2위가 되었다
# 순위 데이터는 순식간에 바뀐다는 것을 코딩을 하다가 알게되었다. 신기한것 같다.
rank1 = rank2.find_previous_sibling("li") #previous_sibling.previous_sibling를 find_previous_sibling으로 간단하게 만들수 있다
print(rank1.a.get_text())
#실행결과 
#연애혁명-323. 마음의 저울

print(rank1.find_next_siblings("li"))   #rank1 기준으로 다음 <li>형제들을 모두 가져온다.


webtoon = soup.find("a",text="간 떨어지는 동거-169. 별거아닌 별 거 4 (마지막화 4)") #a태그 중에 입력한 text를 찾아 <a>태그를 출력한다
print(webtoon)   
#실행결과
#<a href="/webtoon/detail.nhn?titleId=699415&amp;no=170" onclick="nclk_v2(event,'rnk*p.cont','699415','6')" title="간 떨어지는 동거-169. 별거아닌 별 거 4 (마지막화 4)">간 떨어지는 동거-169. 별거아닌 별 거 4 (마지막화 4)</a>

