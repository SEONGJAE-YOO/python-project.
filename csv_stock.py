#코스픽 시가총액 순위 크롤링 하기
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일로 저장하기
filename = "시가총액1-200.csv"
f = open(filename,"w",encoding="UTF-8-sig",newline="") # newline=""을 넣어주어야 작성후 한줄바꾸기가 없어진다.
writer = csv.writer(f) #writer를 이용해서 파일 쓰기
  
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)


for page in range(1,5): #1페이지 부터 5페이지 이전까지 즉 4페이지 까지 출력되게 한다
    res = requests.get(url + str(page))  #page 숫자에서 문자열로 출력하기 위해 str앞에 붙여줌
    res.raise_for_status()   
    soup = BeautifulSoup(res.text,"lxml")  #2:45:08
   
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")      #table 에서 tbody를 가져오고 tbody안에 있는 모든 tr를 가져온다
    #<table summary="코스피 시세정보를 선택한 항목에 따라 정보를 제공합니다." cellpadding="0" cellspacing="0" class="type_2">
    for row in data_rows: #tr안에 있는 td 모두 가져오기 
        columns = row.find_all("td")
        if len(columns) <= 1: #[''] 출력 안되게 하는 해결방안 /의미 없는 데이터는 skip
            continue          # 데이터가 있는 tr은 td가 여러개 이지만 공백이자 보기 좋게 밑줄이 쭉 그어진 tr은 td가 하나만 있다.
                              #<tr><td colspan="13" class="blank_06"></td></tr>  / td가 하나 일때는 아래 코드를 실행하지 않고 건너뛸수 있도록 continue함수 사용한다.

        data = [column.get_text().strip() for column in columns] #columns 있는 정보를 하나씩 가져와서 이름을 column이라고 하고 그 column에서 text를 출력한다. 
        # 따라서 data에는 td가 저장된 각각의 text들이 저장된다.
        #strip() 함수로 '\n\n\t\t\t\t2,000\n\t\t\t\t\n' 불필요한 데이터 제거 하기 
        #strip() 함수를 사용하면 주어진 문자열에 있는 공백과 \n 기호를 삭제시켜 준다
        #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove) 
           
        writer.writerow(data) #csv파일로 저장하기