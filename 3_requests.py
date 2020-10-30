import requests  #requests : Python에서 HTTP 요청을 보내는 모듈
#res =requests.get("http://naver.com")    
res =requests.get("http://google.com")

      
print("응답코드:",res.status_code)#200이면 정상

#웹스크래핑 할때 정상 확인법 1
# if res.status_code == requests.codes.ok:
#      print("정상입니다.")   #꿀팁 : 뛰어쓰기 할때 tab,space 사용하기
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code, "]")


#웹스크래핑 할때 정상 확인법 2
res.raise_for_status() # 웹스크래핑 할때 문제 없이 진행할때 쓰임 ,에러 없다고 표시함
print("웹 스크래핑을 진행합니다")  

print(len(res.text))#가져온 웹페이지의 문자갯수 확인가능

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)      # res.text내용을 mygoogle.html파일로 만들기 
    