#-*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
head ={"user-agent:":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36","Accept-Language":"ko-KR,ko"}   
#실행결과 - 0 이 나와서  "Accept-Language":"ko-KR,ko" 설정해줌 (영어사이트에서 한국언어로 번역해줌)
  
  
  # 구글에서 https://www.whatismybrowser.com/detect/what-is-my-user-agent 검색후 나의 노트북 user-agent 찾기
  #크롤링 할때 컴퓨터가 url접근시 꼭 설정해야지만 크롤링이 된다.(사람이 url접근하는 경우랑 다르다) 
  # get 요청을 보낼때, python requests 로 보내게 되면 몇몇 사이트에서는 로봇이 요청하는것으로 인식해서 응답을 안해주고 차단하는 경우가 있다. 즉, requests로 접근하는 것을 비정상적인 접근으로 보고 차단을 하게 되는것이다.
  #따라서, 이런 경우에는 requests를 호출 할때 User-Agent 를 지정해서 크롬 브라우저에서의 요청인것으로 인식하게 만들어 오류를 해결가능

# #GET REQUEST 예시 1 : url 활용
# res= requests.get(url,hearders =head)
# res.raise_for_status() #브라우저 error 체크 
# soup = BeautifulSoup(res.text, "lxml")

#GET REQUEST 예시 2 : params 활용
PARAMS = {'header':head}   #You need to set header in params: 
pageObj = requests.get(url, params = PARAMS)
soup = BeautifulSoup(pageObj.text,"lxml")  #XML이란 단순한 문자열을 넘어서서, 내부적으로 트리 구조를 가지고 있는 파일을 표현하기 위해 사용하는 마크업 언어입니다. 웹페이지를 보여주기 위해 사용되는 html 파일이 XML의 가장 대표적인 예시입니다. 그런데 그뿐만이 아닙니다. 우리가 친숙하게 사용하는 MS Office의 워드, 엑셀, 파워포인트 파일(docx, xlsx, pptx)도 XML의 일종입니다. 따라서 XML을 해석하는 프로그램(parser라고 부릅니다.)을 미리 준비해야 html, docx, xlsx, pptx와 같이 우리가 흔히 다루는 파일을 처리할 수 있습니다. Python에서 XML parser로서 주로 이용되는 패키지는 lxml입니다. 

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
#<div class="ImZGtf mpg5gc">
print(len(movies))  

# 실행결과 0이 나온 이유 분석 - movie.html를 만들고 나서 확인 해 보니 영어사이트로 들어가졌음  
# with open("movie.html", "w" ,encoding="utf8" ) as f:
#     #f.write(res.text) 
#     f.write(soup.prettify())  #HTML 이쁘게 저장시킴


