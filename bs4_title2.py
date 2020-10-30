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
gauss = soup.find_all("td",attrs={"class":"title"})

for i in range(len(gauss)) :
    title = gauss[i].a.get_text()
    link = gauss[i].a["href"] # gauss[i]객체에서 <a>태그에서 href에 해당하는 것만 가져옴
    print(title)
    print("https://comic.naver.com"+link) #<a href="/webtoon/detail.nhn?titleId=675554&amp;no=911&amp;weekday=mon"  이므로 앞에 https://comic.naver.com를 붙여주여야만 링크를 통해 웹페이지에 들어갈수 있다.

#실행결과 / 링크는 ctrl 누른채로 클릭하면 바로 링크를 통해 웹페이지에 들어갈수 있다.
'''
후기 + 10년 후 가우스
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=911&weekday=mon
시즌4 430화 내일 봐요
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=910&weekday=mon
시즌4 429화 잠행
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=909&weekday=mon
시즌4 428화 추억
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=908&weekday=mon
시즌4 427화 섬세한사람
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=907&weekday=mon
시즌4 426화 적응
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=906&weekday=mon
시즌4 425화 대견
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=905&weekday=mon
시즌4 424화 초빙강사
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=904&weekday=mon
시즌4 423화 추억의 물건
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=903&weekday=mon
시즌4 422화 아니요
https://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=902&weekday=mon

'''