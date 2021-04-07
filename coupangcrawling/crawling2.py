import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

# 여성의류 - 쿠팡랭킹순 모든 상품,가격 가져오기
for idx in range(1, 17):
    url = "http://www.coupang.com/np/categories/498704?page=" + str(idx)

    print(url)
    result = requests.get(url, headers=headers)
    soup_obj = BeautifulSoup(result.content, "html.parser")

    div = soup_obj.findAll("div", {"class": "name"})
    lis = soup_obj.find("ul", {"id": "productList"}).findAll("li")

    for li in lis:
        product = li.find("div", {"class": "name"})
        price = li.find("em", {"class": "sale"}).find(
            "strong", {"class": "price-value"}
        )
        print("여성의류명: " + product.text.strip() + " / " + "상품가격: " + price.text.strip())

## 참고
# enumerate 내장함수 사용하여 Index 출력할 경우
# price_list = list(enumerate(strong))
# for idx, var in enumerate(0):
#     print(idx, var)

# for idx, var in enumerate(strong):
#     print(idx, var)

# CSS를 활용해 select로 찾는 방법
# strong = soup_obj.select(
#     "li > a > dl > dd > div.price-area > div > div.price > em.sale > strong"
# )


#실행결과
'''
여성의류명: 단미들 레오파드 쉬폰 롱 원피스 dm038 / 상품가격: 18,800
여성의류명: 러블로어 2P 세트 그림자고양이 긴팔 티셔츠 / 상품가격: 19,800
여성의류명: 마미누리 804 앞지퍼 서포트 스포츠브라 / 상품가격: 8,850
여성의류명: 오지다 여성용 징포인트 스판 면 팬츠 / 상품가격: 10,900
여성의류명: 가비진 여성용 키작녀 카고 조거 스판 팬츠 / 상품가격: 14,900
여성의류명: 티데일리 남녀공용 베이직 라운드 17수 반팔 티셔츠 / 상품가격: 5,600
여성의류명: 빅걸스토리 여성 빅사이즈 뉴욕 레이어드 오버핏 박스 긴팔티셔츠 / 상품가격: 17,900
여성의류명: 프리티아라 PT3017 블랙 하이웨스트 스키니진 / 상품가격: 19,900
여성의류명: 나타났다 남녀공용 9부 아이스 쿨바지 12종 3+1 / 상품가격: 6,900
여성의류명: [ab.plus] 롱 러플 화이트 스트라이프 셔츠 (LSS4ZB78A) / 상품가격: 28,400
여성의류명: 진마니아 여성용 모던 허리스판 부츠컷 청바지 / 상품가격: 15,210
여성의류명: 캐럿 여성 면 A라인 롱 스커트 / 상품가격: 17,800
여성의류명: 데일리앤 마티아 기본 레이온 긴팔 티셔츠 / 상품가격: 7,700
여성의류명: 이힝 워시 레터링 프린팅 루즈핏맨투맨 봄 맨투맨 / 상품가격: 14,800
여성의류명: 난닝구 스타룬 맨투맨스커트세트 / 상품가격: 29,800
여성의류명: 세이스타일 심플 라운드 H롱 반팔 원피스 / 상품가격: 14,760
여성의류명: 데일로엔 여성용 심플핏 카라 기본 긴팔 티셔츠 / 상품가격: 18,900
여성의류명: 후아유 리버서블 웜업 바람막이 WHJJB1111U / 상품가격: 40,150
여성의류명: 코코블랑 매튜 데님오버롤즈 / 상품가격: 13,900
여성의류명: 포플러앤씨 쉬즈 미디 플리츠 니트 스커트 / 상품가격: 19,800
여성의류명: 헤링본 가을 롱원피스 루즈핏 박시 겨울 플레어 빅사이즈 임산부 HD025 / 상품가격: 28,600
여성의류명: 고스트리퍼블릭 심플 밸런스 디자인 소매 포인트 프린팅 긴팔 라운드 티셔츠 GLT-918 / 상품가격: 16,500
여성의류명: 대박난박양 엘도라도 루즈핏 셔츠 / 상품가격: 19,800
여성의류명: [피트인] 쉐이핑 보정 레깅스 부츠컷 2종택일 요가 필라테스 트레이닝 / 상품가격: 9,900
여성의류명: 블랙캣츠 (Black CATS) (여성)4WAY 스트레치 방풍집업자켓(BC174WJR) / 상품가격: 9,900
여성의류명: [조아맘] MJ™데이즈 스트링 야상 점퍼 JJ04741 / 상품가격: 36,730
여성의류명: 상상그이상 여성용 보석 단추 포인트 라운드 니트가디건 / 상품가격: 27,450
여성의류명: 가비진 여성 쉬폰 플리츠 밴딩 롱치마 224 / 상품가격: 11,610
'''