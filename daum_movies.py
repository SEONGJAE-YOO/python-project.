import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&m=&q=2019%EB%85%84%20%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&nzq=2020%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&DA=NSJ")
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")


images = soup.find_all("img",attrs={"class":"thumb_img"})   
#<img class="thumb_img" src="//search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838" is-person-img="false" width="116" height="164" alt="">