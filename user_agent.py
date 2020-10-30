import requests #rq라고 줄어도 됨
    
url = "http://google.com"
headers = {"user-agent:" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
  # 구글에서 https://www.whatismybrowser.com/detect/what-is-my-user-agent 검색후 나의 노트북 user-agent 찾기
  #크롤링 할때 컴퓨터가 url접근시 꼭 설정해야지만 크롤링이 된다.(사람이 url접근하는 경우랑 다르다) 
  # get 요청을 보낼때, python requests 로 보내게 되면 몇몇 사이트에서는 로봇이 요청하는것으로 인식해서 응답을 안해주고 차단하는 경우가 있다. 즉, requests로 접근하는 것을 비정상적인 접근으로 보고 차단을 하게 되는것이다.
  #따라서, 이런 경우에는 requests를 호출 할때 User-Agent 를 지정해서 크롬 브라우저에서의 요청인것으로 인식하게 만들어 오류를 해결가능
res =requests.get(url, headers={"User-Agent": "Mozilla/5.0"})  #url에 접근할때 user-agent 값 넘겨준다 
res.raise_for_status()     
                             
with open("google.html", "w", encoding="utf8") as f:
    f.write(res.text)      # res.text내용을 파일로 만들기 
                   

   
#ValueError: Invalid header name b'user-agent:' 오류 문제 해결함
#res =requests.get(url, headers=headers) 에서 
#res =requests.get(url, headers={"User-Agent": "Mozilla/5.0"})으로 바꿔주자 오류해결됨