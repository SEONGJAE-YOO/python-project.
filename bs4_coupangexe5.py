#1.광고 제품은 제외하고 리뷰 100개이상 , 평점 4.5 이상 되는 것만 조회
#2.애플 노트북 제외하고 크롤링하기
#3. 3페이지 내에서 크롤링하기
#4. 보기 좋게 제품명,가격,평점,바로가기(링크) 따로 따로 출력하기

#get 
#post 
import requests
import re #정규식 
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}


for i in range(1,4): #1페이지에서 3페이지까지 조회
    # print("페이지 :",i)
     url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
     #page=1 를 page={} 변경하기 / i가 for문으로 인해 1부터 5까지 들어간다
  
     res = requests.get(url ,headers=headers) 
    # 컴퓨터가 url에 접근시에는 user-agent을 사용 해야 한다
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
            #print(" <광고 상품 제외합니다>")
            continue


        name = item.find("div",attrs={"class":"name"}).get_text() #제품명
        #애플 제품 제외
        if "Apple" in name:
           #print(" <Apple 상품 제외합니다>")
            continue
        
        price = item.find("strong",attrs={"class":"price-value"}).get_text() #가격  #<strong class="price-value">458,990</strong>
       
        rate = item.find("em",attrs={"class":"rating"})# 평점 # <em class="rating" style="width:90%">4.5</em>    
        # 평점없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점없는것도 설정해 주어야한다.
        if rate:
            rate =rate.get_text()

        else:  
            #print(" <평점 없는 상품 제외합니다> ")
            continue

        rate_cnt = item.find("span",attrs={"class":"rating-total-count"}) #평점 수    #<span class="rating-total-count">(18)</span>            
        # 평점 수 없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점 수 없는것도 설정해 주어야한다.
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1] #예 : (26)/()제외 하기 위해 범위 지정해주기 
         
        else:  
           #print(" <평점 수 없는 상품 제외합니다>")
            continue

        link = item.find("a",attrs={"class":"search-product-link"})["href"]  
        #<a href="/vp/products/1786054433?itemId=3041108337&amp;vendorItemId=71029166455&amp;q=%EB%85%B8%ED%8A%B8%EB%B6%81&amp;itemsCount=36&amp;searchId=671b89494ceb4626aa547f7273621ced&amp;rank=102" class="search-product-link" >
        # <a>태그에 링크 클래스 속성을 넣어주기
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name,price,rate,rate_cnt)
            print(f"제품명:{name}")
            print(f"가격:{price}")
            print(f"평점:{rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com"+link)) # <a href="/vp/products/1786054433?  ....> 링크 앞에 coupang.com 생략 되있으므로 링크앞에 넣어주기
            print("-"*100) #줄긋기  
              
 
#f-string 사용하기 - python 2에서 지원하던 %-formatting 방식과 format string syntax 인 str.format() 메서드 방식은 가독성 문제때문에 python 3.6이상 부터는 가독성 문제를 해결해 주는 f-string 기능을 제공해준다. 


'''
x = 10
y = 3

f'x + y = {x+y} | x * y = {x*y}'
>>> 'x + y = 13 | x * y = 30'
 매우 간단하게 표현 가능함을 볼 수 있다.

 이를 기존의 %-formatting 과 str.format() 을 사용했을때와 비교해 보자.

# Use %-formatting
'x + y = %d | x * y = %d' %(x+y, x*y)
>>> 'x + y = 13 | x * y = 30'


# Use str.format()
'x + y = {} | x * y = {}'.format(x+y, x*y)
>>> 'x + y = 13 | x * y = 30'
f-string을 사용했을때, 기존의  %-formatting 이나 str.format() 방식보다 훨씬 간결하게 표현 가능한 것을 볼 수 있다.


'''
    
'''     
    <실행결과>
제품명:삼성전자 노트북 플러스 NT550XCJ-K78WA 퓨어 화이트 (i7-10510U 39.6cm), NVMe 256GB, 8GB + 8GB, WIN10 Home
가격:1,379,000
평점:5.0점 (250개)
바로가기 : https://www.coupang.com/vp/products/1459817856?itemId=2511843147&vendorItemId=70504880374
----------------------------------------------------------------------------------------------------
제품명:삼성전자 갤럭시북 이온 노트북 NT950XCJ-X716A 아우라 실버 (i7-10510U 39.6cm MX 250), NVMe 1TB, 16GB, WIN10 Home
가격:2,098,000
평점:4.5점 (125개)
바로가기 : https://www.coupang.com/vp/products/1665436216?itemId=2097917436&vendorItemId=70096804409
----------------------------------------------------------------------------------------------------
제품명:삼성전자 갤럭시북 이온 NT950XCJ-K78A (i7-10510U 39.6cm), 포함, NVMe 256GB + NVMe 256GB, 16GB 
가격:1,889,000
평점:5.0점 (125개)
바로가기 : https://www.coupang.com/vp/products/1137914312?itemId=2517400150&vendorItemId=70510368267
----------------------------------------------------------------------------------------------------
제품명:삼성전자 2020 갤럭시북 플렉스 NT950QCG-X716A (i7-1065G7 39.6cm MX250), NVMe 1TB, 16GB, WIN10 Home
가격:2,598,000
평점:4.5점 (162개)
바로가기 : https://www.coupang.com/vp/products/1665581271?itemId=2097952137&vendorItemId=70096835256
----------------------------------------------------------------------------------------------------
제품명:삼성전자 갤럭시북 이온 NT950XCJ-K78A (i7-10510U 39.6cm), 포함, NVMe 256GB, 16GB
가격:1,819,000
평점:5.0점 (125개)
바로가기 : https://www.coupang.com/vp/products/1137914312?itemId=2108232922&vendorItemId=70107045037
----------------------------------------------------------------------------------------------------
제품명:LG전자 2020 그램15 노트북 15Z995-VR50K (i5-10210U 39.6cm), NVMe 256GB, 8GB, WIN10 Home
가격:1,739,000
평점:5.0점 (173개)
바로가기 : https://www.coupang.com/vp/products/1235351470?itemId=2229827753&vendorItemId=70227443130
----------------------------------------------------------------------------------------------------
'''    