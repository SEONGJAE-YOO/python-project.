# 2015년 부터 2019년 까지 1위부터 5위까지 년대별로 역대 관객 순위 영화 포스터 가져오기 
import requests
from bs4 import BeautifulSoup

  
for year in range(2015,2020): #2015년 부터 2019년 까지 역대 관객 순위 영화 포스터 가져오기
    url = "https://search.daum.net/search?w=tot&m=&q={}%EB%85%84%20%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&nzq=2020%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&DA=NSJ".format(year) #q=2019 부분을 q={} 바꾼다
    res = requests.get(url) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img",attrs={"class":"thumb_img"})   
    #<img class="thumb_img" src="//search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838" is-person-img="false" width="116" height="164" alt="">

    for idx, image in enumerate(images): #루프 돌때마다 idx(인덱스)에 0,1,2,3 등의 주소를 준다. 
        image_url = image["src"]
        if image_url.startswith("//"): # 찾으려고 하는 영화 포스터 사진들이 src="//" 으로 시작하므로 startswith으로 설정해준다
            image_url = "https:" +image_url

        print(image_url)
        # 직접 영화 포스터 url에 접속해서 파일 저장해 보기 
        image_res = requests.get(image_url) # 영화 포스터 url에 접근하기 위해서 requests.get 사용하기
        image_res.raise_for_status()

    
        with open("movie_{}_{}.jpg".format(year,idx+1),"wb") as f:# idx+1를 넣어주므로서 movie1,movie2 으로 저장이 된다.
        # 영화포스터는 텍스트가 아닌 바이너리 파일이므로 "wb"으로 넣어준다.
            f.write(image_res.content) #image_res가 가지고 있는 content정보를 파일로 써준다
      
    
        # 필요한 영화 포스터 이미지만 파일 저장시키는 해결방안 
        if idx >= 4: # 상위 5개 이미지까지만 다운로드 
            break

#실행결과
'''
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F097f7decd11d4a0ae39cb48eade62af63e43724d   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F77746e188b1ca46a1de84b09bf78e67c5c22ce64   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F790095765b452495aef3caf3172a4960ba07e095   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Fcfile76.uf.daum.net%2Fimage%2F2502AF49546B09E61FB5F1
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fbbb263931222d148943c3c2bf3606709d2ee2017   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F38259ef0ed3416ddcc98cd0c30b6f1ad5e5f5f1d  
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fc68515cc88d0227584f67deaa3d0046204ae998b   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fa89c0d7605a29583310a1ba4716bf2d1ccf69bbd   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F9ee4bab1a0f51fb4469b6162bad861f6d25056a7   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F326c4b4cc894250c0bf9356c65110a9f5dc967ca   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fc98cf3e74671b88df0f2b31b516c0aaea2e1a816   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fff9d430c0d2df2a1c659ccba8b621ad2251f6f02   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F404a1310e7b23f39d1472c9a41ac69054753f1dc   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4f9750f09dac0f1b3659ae03cfe9ed7938be8d30   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3620db5faa3faa25e8e48d0e7d2c7601f73277ea   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fe78737f6be1573f673b561f3fc0b32a8cffce820   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fdd84b905224c91225aa2a15203aba3a354197c1d   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fce3cd6a875284e8b96414ef3696756a11544772388211
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3ed58c2c1114935c4cc95f09949acb49b5996fa9   
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fff9d430c0d2df2a1c659ccba8b621ad2251f6f02
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5574fb2c20c844629aa9ad1d6043ee851555464908641
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5afd212b68e34e61a964d969dd898e2f1574298873981
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3673a8a0c5ff4f5c8c25cc959fd6985b1558662957684
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fcab3b02a7b274bd6838b80a5e481fedf1559021787090
'''