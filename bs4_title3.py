import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()  
soup = BeautifulSoup(res.text, "lxml")

gauss = soup.find_all("td",attrs={"class":"title"}) 
'''
#<td class="title"> 속성 모두  찾아서 soup객체에 저장시키고 gauss에 동일하게 저장시킴
<td class="title">
<a href="/webtoon/detail.nhn?titleId=675554&amp;no=911&amp;weekday=mon" onclick="nclk_v2(event,'lst.title','675554','911')">후기 + 10년 후 가우스</a>
</td>
'''
# for gaus in gauss :
#     print(gaus.get_text())

# type(gauss) : class 'bs4.element.ResultSet'
gauss = soup.find_all("div",attrs={"class":"rating_type"})

for i in range(len(gauss)) :
    rate = gauss[i].find("strong").get_text()
    print(rate) 
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
#1:43:11