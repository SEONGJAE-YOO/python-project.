#광고 제품은 제외하고 크롤링하기 
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
    price = item.find("strong",attrs={"class":"price-value"}).get_text() #가격  #<strong class="price-value">458,990</strong>
    
    rate = item.find("em",attrs={"class":"rating"})# 평점 # <em class="rating" style="width:90%">4.5</em>    
    # 평점없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점없는것도 설정해 주어야한다.
    if rate:
       rate =rate.get_text()
    else:  
        rate = "평점 없음"

    rate_cnt = item.find("span",attrs={"class":"rating-total-count"}) #평점 수    #<span class="rating-total-count">(18)</span>            
     # 평점 수 없는 것도 있어 오류가 나온다 그래서 if-else문으로 평점 수 없는것도 설정해 주어야한다.
    if rate_cnt:
       rate_cnt =rate_cnt.get_text()
    else:  
        rate_cnt = "평점 수 없음"
        
    print(name,price,rate,rate_cnt)
 
    '''
 <실행결과>
  <광고 상품 제외합니다>
삼성전자 Flash 노트북 NT530XBB-K24CS (펜티엄 소프트 코랄 N5000 33.7cm), SSD 128GB, 4GB, WIN10 Home 649,000 5.0 (21)
LG전자 2020 울트라 PC 노트북 15U50N-GR36K 화이트 (i3-10110U 39.6cm), SSD 128GB, 8GB, WIN10 Home 763,190 5.0 (6)
레노버 노트북 IdeaPad Slim3-15IML PD 81WB00JAKR (Pantium Gold 6405U 39.624cm WIN미포함 UHD Graphics), 미포함, NVMe 128GB, 4GB 382,200 5.0 (4)
 <광고 상품 제외합니다>
 <광고 상품 제외합니다>
삼성전자 노트북 플러스 NT550XCJ-K78WA 퓨어 화이트 (i7-10510U 39.6cm), NVMe 256GB, 8GB + 8GB, WIN10 Home 1,379,000 5.0 (250)
레노버 ideapad Slim 3 14IIL 3D 노트북 PLATINUM Grey 81WD00MJKR(i3-1005G1 35.5cm), 미포함, NVMe 256GB, 4GB 430,090 3.5 (2)
 <광고 상품 제외합니다>
Apple 2020 맥북 에어 13, Silver, 10세대 i3-1.1GHz dual-core, SSD 256GB, 8GB 1,227,600 5.0 (777)
아이뮤즈 스톰북 15프로 (m3-6y30 39.6cm WIN미포함 8GB eMMC 64GB HD515), StormBook15 PRO, 로즈골드 436,230 4.0 (22)
삼성 노트북 코어i5 SSD탑재 NT200B5B 블랙, 8GB, SSD256G, 윈도우10 349,000 4.0 (77)
LG전자 2020 울트라 PC 노트북 15U50N-GR56K 화이트 (i5-10210U 39.6cm), NVMe 256GB, 8GB, WIN10 Home 943,190 5.0 (23)
LG전자 2019 그램15 노트북 15ZD990-LX10K (팬티엄 5405U 39.6cm), SSD 128GB, 4GB, Free DOS 918,600 5.0 (16)
LG전자 울트라PC 15U50N (펜티엄 39.6cm) + 무선마우스 + 패드 + 노트북가방, 포함, NVMe 256GB, 4GB 739,000 4.5 (6)
삼성전자 갤럭시북 이온 노트북 NT950XCR-A38A 아우라 실버 (i3-10110U 39.6cm), NVMe 256GB, 8GB, WIN10 DSP 1,420,000 4.5 (34)
HP 15S Laptop 노트북 15s-eq0139AU 스노우화이트(라이젠7-3700U 39.62cm WIN미포함 RX Vega 10), 미포함, NVMe 512GB, 8GB 689,010 4.5 (17)
삼성전자 노트북 Plus NT550XCR-AD2A 퓨어 화이트 (펜티엄골드 6405U 39.6cm), NVMe 256GB, 4GB, WIN10 Home 699,000 5.0 (12)
삼성전자 노트북7 NT750XBV-A39A 플래티넘 티탄 (i3-8145U 39.6cm), NVMe 256GB, 8GB, WIN10 Home 999,000 4.5 (83)
삼성전자 노트북 Pen NT930QBE-K37WD Crush White (i3-8145U 33.7cm Win10 Home), 포함, NVMe 256GB, 8GB 1,129,000 4.0 (14)
HP 노트북 15s-fq1075TU (i3-1005G1 39.6cm WIN미포함 UHD Graphics), 미포함, NVMe 256GB, 4GB 509,000 4.5 (41)
에이수스 비보북 르누아르 노트북 M433IA-EB794 (라이젠7-4700U 35.56cm WIN미포함), 미포함, NVMe 512GB, 8GB 848,960 5.0 (11)
에이수스 비보북 노트북 X412FA-EB958 (i5-10210U 35.5cm WIN미포함), 미포함, NVMe 256GB, 8GB 659,000 5.0 (7)
D Graphics), 미포함, NVMe 256GB, 8GB 647,000 5.0 (21)
LG LG그램 LG노트북 i3-6세대 8G SSD256G 14인치 WIN10, 8GB, SSD 256GB, 포함 699,000 4.0 (54)
레노버 ideapad S340-13IML 5D 노트북 81UM003QKR Platinum Grey(i5-10210U 33.7cm WIN미포함), 미포함, SSD 256GB, 8GB 622,330 4.5 (25)
에이수스 VivoBook 노트북 투명 실버 X412FA-EB957(i5-10210U 35.5cm), 미포함, NVMe 256GB, 8GB 664,020 4.5 (2)
LG전자 6세대 코어i5 윈10탑재 LG 그램 14Z960 화이트, 4GB, SSD 256GB, 포함 789,000 평점 없음 평점 수 없음
HP 노트북 15s-fq1003TU (i3-1005G1 39.6cm RAM 4GB SSD 128GB FHD IPS), 스노우 화이트 458,990 4.5 (18)
레노버 아이디어패드 노트북 Platinum Grey S150-11 81VT (Intel Celeron N4020 29.5cm WIN10 Home S), 포함, eMMC 64GB, 4GB 279,000 4.5 (21)
'''