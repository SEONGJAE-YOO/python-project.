from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

browser.find_elements_by_link_text("가는날 선택").click() 
#"가는날 선택" 글자를 통해 찾기
# <a href="javascript:;" ng-hide="" role="button" aria-live="polite" aria-label="" ng-class="{txt_trip_on: searchParams['sdate1'] != ''}" ng-click="onClickCalendar('sdate1')" class="txt_trip ng-binding">가는날 선택</a>

#이번달 27,28일 선택