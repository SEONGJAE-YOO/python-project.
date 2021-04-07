#Step 0. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium import webdriver
import time

query_txt = input('크롤링할 키워드는 무엇입니까?: ')

#Step 1. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://korean.visitkorea.or.kr")
time.sleep(2)  # 위 페이지가 모두 열릴 때 까지 2초 기다립니다.

#코로나 얼럿창 있을 경우 닫기 클릭하기 
#find_element_by_xpath => //:문서내에서 검색,/:절대경로를 나타냄
try :
    driver.find_element_by_xpath('//*[@id="safetyStay1"]/div/div/div/button').click()   
except :
    print("알림창이 없습니다")
    
#Step 2. 검색창의 이름을 찾아서 검색어를 입력합니다
#driver.find_element_by_id("btnSearch").click()

element = driver.find_element_by_id("inp_search")

element.send_keys(query_txt)
element.send_keys("\n")

#Step 3. 검색 버튼을 눌러 실행합니다

#driver.find_element_by_link_text("검색").click()
#driver.find_element_by_class_name("btn_search2").click()  # class name 으로도 가능합니다.
#driver.find_element_by_xpath('//*[@id="gnbMain"]/div/div/div[1]/div[1]/a').click()   # xpath 로도 가능합니다.