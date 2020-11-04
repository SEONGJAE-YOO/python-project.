# 필요없는 블로그 이미지 파일 저장안시키고 필요한 영화포스터만 파일 저장시키기!
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&m=&q=2019%EB%85%84%20%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&nzq=2020%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&DA=NSJ")
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


    with open("movie{}.jpg".format(idx+1),"wb") as f:# idx+1를 넣어주므로서 movie1,movie2 으로 저장이 된다.
    # 영화포스터는 텍스트가 아닌 바이너리 파일이므로 "wb"으로 넣어준다.
        f.write(image_res.content) #image_res가 가지고 있는 content정보를 파일로 써준다
  
  
    # 필요한 영화 포스터 이미지만 파일 저장시키는 해결방안 
    if idx >= 4: # 상위 5개 이미지까지만 다운로드 
        break

#실행결과
'''
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5574fb2c20c844629aa9ad1d6043ee851555464908641
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5afd212b68e34e61a964d969dd898e2f1574298873981
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3673a8a0c5ff4f5c8c25cc959fd6985b1558662957684
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fcab3b02a7b274bd6838b80a5e481fedf1559021787090
'''
