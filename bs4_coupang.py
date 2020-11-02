#get 
#post 
import requests
import re #정규식 
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
res = requests.get(url ,headers=headers) # 컴퓨터가 url에 접근시에는 user-agent 사용 해야한다
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li",attrs={"class":re.compile("^search-product")}) 
#<li class="search-product " 이므로 li태그 중에서 클래스 정보가 search-product으로 시작하는 모든 li정보를 다가져온다

#print(items[0].find("div",attrs={"class":"name"}).get_text())     #<div class="name">HP 노트북 15s-fq1003TU (i3-1005G1 39.6cm RAM 4GB SSD 128GB FHD IPS), 스노우 화이트</div>
#실행결과 -HP 노트북 15s-fq1003TU (i3-1005G1 39.6cm RAM 4GB SSD 128GB FHD IPS), 스노우 화이트

for item  in items:
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
(실행결과)
삼성전자 노트북 플러스 플래티넘 티탄 NT550XCR-AD1A (셀러론-5205U 39.6cm WIN10 Home), 포함, NVMe 128GB, 8GB 697,000 3.5 (3)
레노버 울트라북 ThinkPad T440 4세대i5 8G램 SSD 256G 정품 윈도우10 Pro 업그레이드, 8GB, SSD 256GB 329,000 평점 없음 평점 수 없음
레노버 ideapad Slim 3 14IIL 3D 노트북 ABYSS BLUE 81WD00MLKR(i3-1005G1 35.5cm), 미포함, NVMe 256GB, 4GB 430,090 1.0 (1)
LG전자 2020년 울트라PC 노트북 13UD50N-GX50K (i5-10210U 33.7cm), NVMe 256GB, 8GB, Free DOS 728,090 4.0 (2)
LG전자 울트라PC 노트북 화이트 15UD40N-GX56K (라이젠5-4500U 39.6cm), 미포함, NVMe 256GB, 8GB 764,090 5.0 (31)
HP [주문당일출고] 15s-fq1075TU 다운로드 쿠폰할인 한컴오피스증정 Nvme256GB 인텔10세대 i3 윈도우10프로 탑재, 8GB, Nvme SSD 256GB, 포함 659,000 4.5 (42)
삼성전자 노트북7 NT750XBV-A39A 플래티넘 티탄 (i3-8145U 39.6cm), NVMe 256GB, 8GB, Linux 899,000 4.5 (83)
LG전자 울트라PC 노트북 15UD50N-GX30K (i3-10110U 39.6cm), 미포함, SSD 128GB, 8GB 728,000 5.0 (7)
삼성전자 삼성노트북 i5-3세대 8G SSD240G 15.6인치 WIN10, SSD 240GB, 8GB, 포함 379,000 4.0 (7)
중고노트북 10만원대 삼성 LG HP 등, 단일색상, [A] 레노버EDGE 109,000 4.0 (34)
LG전자 울트라PC 17U790-GA76K (i7-8565U 43.1cm) + 무선마우스 + 키스킨 + 마우스 패드 + HDMI 케이블, NVMe 256GB, 8GB, WIN10 Home 1,298,990 4.5 (3)      
에이수스 젠북 노트북 라일락미스트 UM425IA-AM002 (라이젠5-4500U 35.56cm), 미포함, NVMe 512GB, 8GB 849,000 5.0 (1)
LG 그램14 노트북 스노우화이트 14ZD995-LX20K (펜티엄-6405U 35.5cm), 미포함, M.2 128GB, 4GB 909,000 평점 없음 평점 수 없음
LG전자 2020년 그램17 노트북 17ZD90N-VX5BK (i5-1035G7 43.1cm), NVMe 256GB, 8GB, Free DOS 1,436,410 5.0 (53)
레노버 노트북 Platinum Grey Flex 5 14IIL i5 W10 (i5-1035G1 35.5cm WIN10 Home), 포함, NVMe 256GB, 8GB 889,220 4.5 (3)
아이뮤즈 스톰북 노트북 STOMBOOK (셀러론 N3350 35.814cm WIN10 Home), 포함, eMMC 64GB + SSD 256GB, 4GB 435,000 4.0 (1)
레노버 아이디어패드 노트북 플래티넘그레이 S340-13IML 3D (10세대 i3-10110U 33.7cm WIN미포함), 미포함, SSD 256GB, 8GB 537,190 4.0 (17)
LG전자 그램15 노트북 15ZD995-VX70K 스노우 화이트 (i7-10510U 39.6cm), NVMe 256GB, 8GB, Free DOS 1,492,310 5.0 (4)
LG전자 울트라 PC 노트북 15U70N-GR56K 다크실버 (i5-10210U 39.6cm), NVMe 256GB, 8GB, WIN10 Home 1,098,000 5.0 (30)
LG 울트라PC 15U560 6세대 i5 지포스940M 15.6인치 윈도우10, SSD 256GB + HDD 500GB, 8GB, 포함 645,000 4.5 (9)
LG 그램 14Z950 5세대 i5 14인치 윈도우10, 8GB, SSD256GB, 포함 649,000 3.5 (5)
삼성전자 갤럭시북 플렉스 알파 노트북 NT750QCR-A58A-X16G (i5-10210U 39.6cm), 미포함, NVMe 256GB, 16GB 1,667,000 5.0 (4)
삼성전자 갤럭시북 이온 노트북 NT950XCJ-X716A 아우라 실버 (i7-10510U 39.6cm MX 250), NVMe 1TB, 16GB, WIN10 Home 2,098,000 4.5 (125)
에이서 아스파이어5 블랙 N19C3 (피카소 R5-3500U 39.6cm IPS FHD AMD 라데온 Vega8 백라이트 키보드 WIN10), 포함, SSD 128GB, 4GB 649,000 4.5 (5)
레노버 ThinkBook 15-IIL 노트북 미네랄 그레이 20SMA00CKR (10세대 i7-1065G7 39.6cm WIN 10 Pro), 포함, NVMe 512GB, 16GB 1,199,000 5.0 (4)
레노버 노트북 YOGA C340-15IIL i7 Pen X 81XJ0020KR (i7-1065G7 39.6cm WIN10 Home IRIS PLUS), 포함, SSD 256GB, 8GB 999,000 5.0 (4)
레노버 ThinkPad E495-S0J8 (AMD 라이젠5 35.6cm WIN미포함 RAM 8GB SSD 128GB AMD 라데온 Vega8), Free DOS, 256GB, E495-SOJ8, 블랙 629,000 4.5 (23)
삼성전자 갤럭시북 플렉스 알파 노트북 NT750QCR-A38A (i3-10110U 39.6cm WIN10 Home), 포함, NVMe 256GB, 16GB 1,579,000 5.0 (56)
삼성전자 삼성노트북 슬림 i5-4세대 8G SSD256G 13인치 WIN10, 8GB, SSD 256GB, 포함 529,000 5.0 (12)
한성컴퓨터 노트북 블랙 언더케이지 TFX245S (i5-10210U 35.56cm WIN미포함), 미포함, NVMe 500GB, 8GB 749,000 5.0 (70)
LG전자 2020 그램 2in1 노트북 14TD90N-VX50K (i5-10210U 35.5cm), NVMe 256GB, 8GB, Free DOS 1,389,040 4.5 (47)
삼성전자 갤럭시북 S NT767XCM-K58 Earth Gold (Wi-Fi전용 i5-L16G7 33.7cm Win10 Home)+파우치+한컴오피스, 포함, eUFS 256GB, 8GB 1,299,000 4.5 (10)
HP [주문당일출고] 15s-fq1075TU 메모리 4GB 무상 업그레이드 한컴오피스증정 윈도우10프로 탑재, 8GB, 256GB SSD NVMe M.2, 포함 659,000 5.0 (24)
LG전자 울트라PC 노트북 17UD70N-GX76K (i7-10510U 43.1cm UHD Graphics), 미포함, NVMe 256GB, 8GB 1,275,360 5.0 (7)
삼성전자 갤럭시북 이온 NT950XCJ-K78A (i7-10510U 39.6cm), 포함, NVMe 256GB + NVMe 256GB, 16GB 1,859,000 5.0 (125)
아이뮤즈 스톰북 15프로 (m3-6y30 39.6cm WIN10 8GB eMMC 64GB), StormBook15 PRO, 로즈골드 638,000 4.5 (9)
'''