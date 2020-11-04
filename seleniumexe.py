#[python] Selenium으로 스크래핑하기
#1. pip install selenium 터미널에서 설치하기
#selenium은 WebBrowser(Chrome, Firefox, IE, Safari 등등)를 조작해주는 Framework로, 작동원리는 조작을 원하는 Browser가 설치된 PC에 Browser를 조작해줄 수 있는 webdriver(조작을 원하는 browser별로 실제 파일이 다름)를 다운받은 후 해당 webdriver가 실행되면 서버처럼 구동된다.
#2. 크롬에서 검색창에 chrome://version/ 입력 후 86.0.4240.111 크롬 버전 확인해주기
#3. https://chromedriver.chromium.org/downloads 에서 크롬 버전에 맞는 드라이버 설치해주기
#4. 쓰고 있는 현재 폴더에 크롬 드라이버 압축 풀기 

# 네이버 들어가서 네이버 로그인 페이지 열어보기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #입력한 글자를 검색하는 모듈 사용함 

browser =webdriver.Chrome("./chromedriver.exe") # 현재 폴더에 쓰고 있으므로 현재 폴더 주소 넣기 
                                                # 다른 폴더에 크롬드라이버가 있으면 다른 폴더 주소 넣어주기
browser.get("http://naver.com")  # 크롬 웹 드라이버 객체를 생성하고 그 browser에서 넣어준 url로 접근한다.
elem =browser.find_element_by_class_name("link_login") #네이버 아이디 로그인 하기 
#<a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https%3A%2F%2Fwww.naver.com" class="link_login" data-clk="log_off.login"><i class="ico_naver"><span class="blind">네이버</span></i>로그인</a>
#class="link_login" 이므로 "link_login" 넣어주기 
#find_element_by_class_name(name)는 클래스 이름이 name에 해당하는 요소를 하나 추출할때 사용함

elem.click()   
#browser.back() #브라우저 전 페이지로 이동
#browser.forward()  #브라우저 앞에 페이지로 이동
#browser.refresh()  # 브라우저 새로고침


