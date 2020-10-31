import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()  
soup = BeautifulSoup(res.text, "lxml")
      
gauss = soup.find_all("div",attrs={"class":"rating_type"})
'''
# html 코드 안에 있는 <div> 클래스가 rating_type인  속성 모두 찾아 soup에 저장시킨다.
<div class="rating_type">
<span class="star"><em style="width:99.81%">평점</em></span>
	<strong>9.98</strong>
</div>
'''
for i in range(len(gauss)) :   # <div class="rating_type">들 안에서 <strong>9.98</strong> 부분을 모두 찾아낸다.
    rate = gauss[i].find("strong").get_text()  # 모두 찾아내서 text부분만 get하여 gauss[i]에 저장시킴
    print(rate) # gauss[i]를 출력시킴 
#실행결과
'''
9.98
9.98
9.97
9.97
9.97
9.98
9.97
9.97
9.97
9.97
'''
