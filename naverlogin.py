import time #자동입력 방지문자 때문에 써줌
from selenium import webdriver

browser = webdriver.Chrome() # "./chromedriver.exe"

# 1.네이버 이동 
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login") # 네이버 페이지에서 네이버로그인 버튼이 class="link_login"이므로 "link_login" 넣어주기
#<a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https%3A%2F%2Fwww.naver.com" class="link_login" data-clk="log_off.login"><i class="ico_naver"><span class="blind">네이버</span></i>로그인</a>
elem.click()

# 3. id ,pw 입력
browser.find_element_by_id("id").send_keys("yousong4243")
#<input type="text" id="id" name="id" accesskey="L" placeholder="아이디" class="int" maxlength="41" value="">
time.sleep(3)
browser.find_element_by_id("pw").send_keys("qncjfmlakd123!!!")
#<input type="password" id="pw" name="pw" placeholder="비밀번호" class="int" maxlength="16">

#로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
#<input type="submit" title="로그인" alt="로그인" value="로그인" class="btn_global" id="log.login">
time.sleep(3)

# id 새로 입력
#browser.find_elements_by_id("id").clear() # 3초 있다가 "naver_id" 지우고 "my_id"로 바꾼다 
#browser.find_elements_by_id("id").send_Keys("my_id") 

# html 정보 출력
print(browser.page_source)  

# 브라우저 종료
#browser.close() #현재 탭만 종료
browser.quit() # 전체 브라우저 종료
