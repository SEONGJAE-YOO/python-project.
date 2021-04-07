#Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium import webdriver
import time
import sys
#sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

query_txt = input('크롤링할 키워드는 무엇입니까?: ')
f_name = input('검색 결과를 저장할 파일경로와 이름을 지정하세요(예:c:\\data\\test.txt): ')

#Step 2. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://korean.visitkorea.or.kr/main/main.html")
time.sleep(2)  #  창이 모두 열릴 때 까지 2초 기다립니다.

#코로나 얼럿창 있을 경우 닫기 클릭하기 
#find_element_by_xpath => //:문서내에서 검색,/:절대경로를 나타냄
try :
    driver.find_element_by_xpath('//*[@id="safetyStay1"]/div/div/div/button').click()   
except :
    print("알림창이 없습니다")
    
       
#Step 3. 검색창의 이름을 찾아서 검색어를 입력하고 검색을 실행합니다
#driver.find_element_by_id("btnSearch").click()
element = driver.find_element_by_id("inp_search")
element.send_keys(query_txt)

driver.find_element_by_link_text("검색").click()

# 학습목표 1: 텍스트를 추출하여 화면에 출력하기
# Step 4. 현재 페이지에 있는 내용을 화면에 출력하기

time.sleep(1)

full_html = driver.page_source

soup = BeautifulSoup(full_html, 'html.parser')

content_list = soup.find('ul','list_thumType type1')

for i in content_list:
    print(i.text.strip())
    print("\n")
 

 # 학습목표 2: 텍스트를 추출하여 txt 형식으로 저장하기
# Step 5. 현재 페이지에 있는 내용을 txt 형식으로 파일에 저장하기
orig_stdout = sys.stdout
f = open(f_name , 'a' , encoding='UTF-8')
sys.stdout = f
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul',class_='list_thumType type1')

for i in content_list:
    print(i.text.strip())
    print("\n")
    
sys.stdout = orig_stdout
f.close()

print(" 요청하신 데이터 수집 작업이 정상적으로 완료되었습니다")



'''
1.TypeError: 'NoneType' object is not iterable 해결방법

57줄 /content_list = soup.find('ul',class_='list_thumType type1')
클래스 이름 잘못 입력함
'''