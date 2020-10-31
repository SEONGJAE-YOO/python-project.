#네이버 이미지 검색결과 한번에 다운로드 하는 방법
from urllib.request import urlopen
from urllib.parse import quote_plus  #HTTP 요청, 파싱과 관련된 하위 패키지들이 존재하며, URL 파싱과 관련된 것들은 거의 다 urllib.parse에 들어 있다
from bs4 import BeautifulSoup  #터미널에서 pip install bs4 으로 설치해준다 
    
baseurl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query='
plusurl = input("검색어를 입력하세요:")
url = baseurl + quote_plus(plusurl)  #검색어를 아스키 코드로 변환시켜주는 quote_plus 사용함
#print(url)

html = urlopen(url).read() #urlopen 함수는 웹에서 얻은 데이터에 대한 객체를 반환해 준다 / read()을 통해 html 코드를 가져온다
soup =BeautifulSoup(html,'html.parser') #html를 분석해줄수 있게 BeautifulSoup 사용함
img = soup.find_all(class_='_img') #이미지 모두 가져올수 있게 find_all() 사용함
                                 # <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2Fdata2%2F2004%2F2%2F5%2F69%2F%25B5%25FE%25B1%25E2%25BB%25E7%25C1%25F83.jpg&amp;type=b400" class="_img"
                                  # src 뒷부분 class="_img"를 넣어준다. 단 class만 쓰면 오류나서 class_으로 넣어준다.

n = 1
for i in img:
    imgUrl= i['data-source'] #jsp에서 db커넥션 역할을 하는 datasource 넣어준다
    with urlopen(imgUrl) as f: #with ... as 구문을 사용하게 되면 파일을 열고 해당 구문이 끝나면 자동으로 닫히게 된다. /파일스트림 기능
     with open(plusurl+str(n)+'.jpg','wb') as h: #이미지 저장시 검색어이름으로 저장하게 한다. 예를 들어 과일을 검색하면 과일1,과일2,과일3으로 저장된다./ 이미지파일이 바이너리파일이므로 wb를 넣어준다
           img = f.read()  #읽어와서 img변수안에 저장
           h.write(img)#파일명을 쓴다
    n +=1
   
print("다운로드 완료")
