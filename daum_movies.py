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

# 실행결과 - 영화포스터 만 파일 저장 시키는게 아닌 밑에 블로그 이미지 까지 저장 시킨다. 필요없는 이미지는 저장 안시키도록 해야겠다.
'''
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4e00e81f2b6f4d2eb65b3387240cc3c01547608409838
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5574fb2c20c844629aa9ad1d6043ee851555464908641
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F5afd212b68e34e61a964d969dd898e2f1574298873981
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3673a8a0c5ff4f5c8c25cc959fd6985b1558662957684
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fcab3b02a7b274bd6838b80a5e481fedf1559021787090
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F840094b1d3714d98a3f1841cac3b82d81563931141135
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F984467734d0441d9bd342456607cefe31558926997358
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fc8555d7906ba4559a1290c616e416c4c1576742973513
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F9633f50f32a34df2ae91dbac1203062e1551065947586
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F0357a82b7226464b87072c0b8d2246b71567986846719
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fcc2179cd2bfc46ed84d285086339f2321563514510944
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F1f887bf800ac4d63be45d94bc9ddeac51563411889783
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F817749999554400daebc36f51c16b2901565673492583
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fcc7165f75bb94140a95d977881cebc191571895256827
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F68697a4b31e7461b8ffe3211a9cd12b31564105313046
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fda2e6f0663514ba3aaf1f003733d08831560262646934
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fdca667637a164f01b556a8d6b8277ef41551836200950
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F27a31d4c5a0540ea86cd0237dccc49d51557888570172
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F08603eebe4e740e9a19384f0a0f5cfed1568165443925
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F02efc2364d924115880baf78fd6e9d4a1545286152910
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F3e6591d23bbc4f8986f4dce958afac4d1551150359176
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F33f6b51372e94272a2b802d6e1b3cc321576635274939
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Ffbe0d4ccc4804448a8aacb9e98ccccfe1573614596648
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F9d20cf3485cc4602ad59e418870dcd291572404771686
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F400a8860f56e4ce79425c06de79c11001548636701111
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fc718986ee7284fe6899244115cdbd0211566460622237
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F88c944d4893a41f4b9131a53a4320c241572311557066
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F849edb91f7034d338709526e3647c2dd1548391120712
https://search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Fmovie%2F4295e3725db4457a8c9d810416c7e7741543894164660
#너무 많아 생략합니다.
'''