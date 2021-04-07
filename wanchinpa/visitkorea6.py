#Chap 7-1. 이미지 다운로드용 웹크롤러 만들기
# Step 1. 필요한 모듈과 라이브러리를 로딩하고 검색어를 입력 받습니다
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import urllib
import time
import sys
import re
import math
import os
import random

f_dir = input('사진을 저장할 폴더를 지정하세요(예: c:\data\) : ')
query_txt ='사진저장'

#Step 2. 파일을 저장할 폴더를 생성합니다
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

os.chdir(f_dir)
os.makedirs(f_dir+s+'-'+query_txt)
os.chdir(f_dir+s+'-'+query_txt)
f_result_dir = f_dir+s+'-'+query_txt

#Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
path = "C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver"
driver = webdriver.Chrome(path)

s_time = time.time( )      # 크롤링 시작 시간을 위한 타임 스탬프를 찍습니다

driver.get("https://korean.visitkorea.or.kr/detail/rem_detail.html?cotid=be3db10c-b642-409c-81cc-c4cdecb5bd8b&temp=")
time.sleep(2)  # 페이지가 모두 열릴 때 까지 2초 기다립니다.

# 학습목표 1: 자동 스크롤다운 함수 만들기
# Step 4.  스크롤다운 함수를 생성한 후 실행합니다.
def scroll_down(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(1)
    
scroll_down(driver) 
    

# 본문의 사진 정보를 가져와서 지정된 폴더에 저장하기    
# Step 5. 이미지 추출하여 저장하기 

file_no = 0                                
count = 1
img_src2=[]    

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
img_src = soup.find('div','box_txtPhoto').find_all('img')

for i in img_src :
        img_src1=i['src']
        img_src2.append(img_src1)
        count += 1

for i in range(0,len(img_src2)) :
        try :
                urllib.request.urlretrieve(img_src2[i],str(file_no)+'.jpg')
        except :
                continue        
        file_no += 1                
        time.sleep(0.5)      
        print("%s 번째 이미지 저장중입니다=======" %file_no)
       
# Step 6. 요약 정보를 출력합니다                
e_time = time.time( )
t_time = e_time - s_time

store_cnt = file_no -1

print("=" *70)
print("총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("총 저장 건수는 %s 건 입니다 " %file_no)
print("파일 저장 경로: %s 입니다" %f_result_dir)
print("=" *70)

driver.close( )