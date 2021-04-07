# Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium import webdriver
import time
import sys

query_txt = input('크롤링할 키워드는 무엇입니까?: ')
f_name = input('검색 결과를 저장할 txt 파일경로와 이름을 지정하세요(예:c:\\data\\test_3.txt): ')
fc_name = input('검색 결과를 저장할 csv 파일경로와 이름을 지정하세요(예:c:\\data\\test_3.csv): ')
fx_name = input('검색 결과를 저장할 xls 파일경로와 이름을 지정하세요(예:c:\\data\\test_3.xls): ')

#Step 2. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://korean.visitkorea.or.kr/main/main.html")
time.sleep(2)  

#코로나 얼럿창 있을 경우 닫기 클릭하기 
try :
    driver.find_element_by_xpath('//*[@id="safetyStay1"]/div/div/div/button').click()
except :
    print("코로나 창이 없습니다")
    
#Step 3. 검색창의 이름을 찾아서 검색어를 입력 후 검색을 진행합니다
element = driver.find_element_by_id("inp_search")
element.send_keys(query_txt)
driver.find_element_by_link_text("검색").click()

# Step 4. 현재 페이지에 있는 내용을 화면에 출력하기

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul',class_='list_thumType type1')
#print(content_list)

# 1: 특정 항목들을 분리해서 추출하기
contents = content_list.find('div','tit').get_text( )
print('제목:',contents.strip())
    
tag = content_list.find('p','tag_type').get_text()
print('해쉬태그:',tag.strip())
print("\n")

# Step 5. 각 항목별로 분리하여 추출하고 변수에 할당하기
no = 1
no2 =[ ]
contents2=[ ]
tags2=[ ]

for i in content_list:
    no2.append(no)
    print('번호:',no)
    
    contents = i.find('div','tit').get_text()
    contents2.append(contents)
    print('내용:',contents.strip())
    
    tag = i.find('p','tag_type').get_text()
    tags2.append(tag)
    print('태그:',tag.strip())
    print("\n")
    
    no += 1
    if no == 4:
     break

# 2: 분리 수집된 데이터를 데이터 프레임으로 만들어서 
# csv , xls 형식으로 저장하기
  
# 출력 결과를 표(데이터 프레임) 형태로 만들기
import pandas as pd

korea_trip = pd.DataFrame()
korea_trip['번호']=no2
korea_trip['내용']=contents2
korea_trip['태그']=tags2

# csv 형태로 저장하기
korea_trip.to_csv(fc_name, encoding="utf-8-sig")
print(" csv 파일 저장 경로: %s" %fc_name)

# 엑셀 형태로 저장하기
import xlwt   # pip install xlwt 실행 후 수행
korea_trip.to_excel(fx_name)
print(" xls 파일 저장 경로: %s" %fx_name)

# 출력 결과를 txt 파일로 저장하기
f = open(f_name, 'a',encoding='UTF-8')
f.write(str(contents2))
f.write(str(tags2))
f.close( )
print(" txt 파일 저장 경로: %s" %f_name)  


