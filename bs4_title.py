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
for gaus in gauss :
    print(gaus.get_text())
#실행결과
'''
후기 + 10년 후 가우스


시즌4 430화 내일 봐요


시즌4 429화 잠행


시즌4 428화 추억


시즌4 427화 섬세한사람


시즌4 426화 적응


시즌4 425화 대견


시즌4 424화 초빙강사


시즌4 423화 추억의 물건


시즌4 422화 아니요
'''