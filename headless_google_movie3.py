# headless으로 매번 브라우저 띄우는 것 안하고 (메모리 차지 안함)
#백그라운드에서 실행된다.
from selenium import webdriver

# headless chrome 
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920*1080") # 1920*1080 크기에 맞춰서 브라우저를 띄어 내부적으로 동작하게 끔 함
# 4:20:15
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url ="https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_elements_by_id("detected_value") #<div> 태그 id 값을 넣어줌
#<div class="value" id="detected_value"><a href="https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36</a></div>
#print(detected_value.text)


# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

import time
interval = 2 # 4초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollheght")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollheght")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")
                

import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
    # 활인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "활인되지 않은 영화 제외")
        continue

    # 활인된 가격  /<span class="VfPpfd ZdBevf i5DZme"><span>₩7,000</span></span>
    price = movie.find("span", attrs={"class", "VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 /<a href="/store/movies/details/%EA%B2%A8%EC%9A%B8%EC%99%95%EA%B5%AD_2_%EC%9E%90%EB%A7%89%ED%8C%90?id=9kTBYkw3zH8" aria-hidden="true" tabindex="-1" class="JC71ub"></a>
    link = movie.find("a", attrs={"class":"JC71ub"})["href"] #모든 영화 포스터 링크들이 클래스가 "JC71ub"이다
    # "https://play.google.com" + link

    print(f"제목 : {title}")
    print(f"할인 전 가격 : {original_price}")
    print(f"할인 후 가격 : {price}")
    print("링크 : " + "https://play.google.com" + link)
    print("-" * 100)

    browser.quit()


'''   
#실행결과

'''