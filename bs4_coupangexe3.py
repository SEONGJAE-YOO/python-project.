#광고 제품은 제외하고 리뷰 100개이상 , 평점 4.5 이상 되는 것만 조회
#애플 노트북 제외하고 크롤링하기

#get 
#post 
import requests
import re #정규식 
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
res = requests.get(url ,headers=headers) # 컴퓨터가 url에 접근시에는 user-agent 사용 해야한다
res.raise_for_status()  
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li",attrs={"class":re.compile("^search-product")}) 
#<li class="search-product " 이므로 li태그 중에서 클래스 정보가 search-product으로 시작하는 모든 li정보를 다가져온다

#print(items[0].find("div",attrs={"class":"name"}).get_text())     #<div class="name">HP 노트북 15s-fq1003TU (i3-1005G1 39.6cm RAM 4GB SSD 128GB FHD IPS), 스노우 화이트</div>
#실행결과 -HP 노트북 15s-fq1003TU (i3-1005G1 39.6cm RAM 4GB SSD 128GB FHD IPS), 스노우 화이트

for item  in items:

    #광고 제품은 제외   #<span class="ad-badge-text">광고</span>
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다>")
        continue


    name = item.find("div",attrs={"class":"name"}).get_text() #제품명
    #애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue
    
    price = item.find("strong",attrs={"class":"price-value"}).get_text() #가격  #<strong class="price-value">458,990</strong>
    
    rate = item.find("em",attrs={"class":"rating"})# 평점 # <em class="rating" style="width:90%">4.5</em>    
    # 평점없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점없는것도 설정해 주어야한다.
    if rate:
       rate =rate.get_text()

    else:  
        print(" <평점 없는 상품 제외합니다> ")
        continue
  
    rate_cnt = item.find("span",attrs={"class":"rating-total-count"}) #평점 수    #<span class="rating-total-count">(18)</span>            
     # 평점 수 없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점 수 없는것도 설정해 주어야한다.
    if rate_cnt:
       rate_cnt = rate_cnt.get_text() #예 : (26)
       rate_cnt = rate_cnt[1:-1] #()제외 하기 위해 범위 지정해주기 
      # print("리뷰 수",rate_cnt) 
    else:  
        print(" <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
         print(name,price,rate,rate_cnt)
   
   
 
    '''
 <실행결과>
삼성전자 노트북 플러스 NT550XCJ-K78WA 퓨어 화이트 (i7-10510U 39.6cm), NVMe 256GB, 8GB + 8GB, WIN10 Home 1,379,000 5.0 250
 <Apple 상품 제외합니다>     
 <평점 없는 상품 제외합니다> 
 <평점 없는 상품 제외합니다> 
 <평점 없는 상품 제외합니다> 

  '''