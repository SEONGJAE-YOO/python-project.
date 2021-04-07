# Step 0. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup     
from selenium import webdriver
import pandas as pd
import time
import sys
import xlwt


f_name = input('검색 결과를 저장할 txt 파일경로와 이름을 지정하세요(예:c:\\data\\test.txt): ')
fc_name = input('검색 결과를 저장할 csv 파일경로와 이름을 지정하세요(예:c:\\data\\test.csv): ')
fx_name = input('검색 결과를 저장할 xls 파일경로와 이름을 지정하세요(예:c:\\data\\test.xls): ')

#Step 1. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver"
driver = webdriver.Chrome(path)
  
s_time = time.time( )      # 크롤링 시작 시간을 위한 타임 스탬프를 찍습니다

driver.get("https://korean.visitkorea.or.kr/detail/rem_detail.html?cotid=be3db10c-b642-409c-81cc-c4cdecb5bd8b&temp=")
time.sleep(2)  # 페이지가 모두 열릴 때 까지 2초 기다립니다.

# 학습목표 1: 본문에서 상세한 텍스트 내용 출력하기
# Step 2. 현재 페이지에 있는 상세 텍스트 내용을 추출하기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find_all('div','txt_p')

# 데이터를 저장하기 위한 리스트 생성
contents2 = [ ]
tags2 = [ ]
no = 1
no2 = [ ]
# 본문 내용 수집하기
print("\n")
print("데이터 추출을 시작합니다==================================")
print("\n")

f = open(f_name, 'a',encoding='UTF-8')

for i in content_list:

    no2.append(no)
    print('1.번호:',no)
    cont = i.get_text().replace("\n","")
    contents2.append(cont)
    f.write(str(cont) + "\n")
    print(cont)
    print("\n")
    
    no += 1
# 태그 정보 찾기 
tag_list = soup.find_all('ul','tag clfix')

tags2 =[]
for i in tag_list:
    print("\n")
    tag = i.get_text()
    tags2.append(tag)
    f.write(str(tag))
    print(tag)

f.close( )

# 학습목표 2: 출력된 결과를 파일로 저장하기
# Step 3. 다양한 파일 형식으로 저장하기
# 출력 결과를 표(데이터 프레임) 형태로 만들기


korea_trip = pd.DataFrame()
korea_trip['번호']=no2
korea_trip['내용']=pd.Series(contents2)
korea_trip['태그']=pd.Series(tags2)

# csv 형태로 저장하기
korea_trip.to_csv(fc_name,encoding="utf-8-sig" , index=False)

# 엑셀 형태로 저장하기
korea_trip.to_excel(fx_name , index=False)

# Step 4. 요약 정보 보여주기
e_time = time.time( )     # 검색이 종료된 시점의 timestamp 를 지정합니다
t_time = e_time - s_time

print("\n") 
print("=" *80)
print("총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("파일 저장 완료: txt 파일명 : %s " %f_name)
print("파일 저장 완료: csv 파일명 : %s " %fc_name)
print("파일 저장 완료: xls 파일명 : %s " %fx_name)
print("=" *80)

driver.close( )