import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re   


ID = 'yousong4243@daum.net' #인스타그램 ID
PW = 'tjdwo357' #인스타그램 PW

#화면 띄우기
browser = wd.Chrome('C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver')
browser.get("https://instagram.com")

#로딩하는 시간 기다리기
time.sleep(2)

#Login ID 속성값 찾고 입력하기
login_id = browser.find_element_by_name('username')
login_id.send_keys(ID)

#Login PW 속성값 찾기 입력하기
login_pw = browser.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

keyword = "공차"

url = "https://www.instagram.com/{}/".format(keyword)

instagram_tags = [] 
instagram_tag_dates = []



browser.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click() 
for i in range(76086): 
    time.sleep(2) 
    try: 
        data = browser.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj
        tag_raw = data.text 
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw) 
        tag = ''.join(tags).replace("#"," ") # "#" 제거 
        
        tag_data = tag.split() 
        
        for tag_one in tag_data: 
            instagram_tags.append(tag_one) 
            # print(instagram_tags) 
        
        date = browser.find_element_by_css_selector("time.FH9sR.Nzb55" ).text # 날짜 선택 
        
        if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1: 
            instagram_tag_dates.append('0주') 
        else: 
            instagram_tag_dates.append(date)
             #print(instagram_tag_dates) 
    except: 
            instagram_tags.append("error") 
            instagram_tag_dates.append('error') 
    try: 
        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow'))) 
        browser.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click() 
    except: 
        browser.close() 
    # date = datum2.text 
    #print(date) 
    time.sleep(3) 
browser.close()
