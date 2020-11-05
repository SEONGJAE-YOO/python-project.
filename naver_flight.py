from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some convenience methods provided that help you write code that will wait only as long as required. WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.
#명시적인 대기는 특정 조건이 발생하는 것을 기다린 후 코드를 계속하도록 정의하는 코드입니다. 이 극단적 인 경우는 time.sleep ()에서이 조건을 정확한 대기 시간을 설정합니다. 필요한 시간 동안 대기하는 코드를 작성하는 데 도움이되는 편리한 메소드들이 제공되고 있습니다. WebDriverWait와 ExpectedCondition를 함께 이를 구현하는 하나의 방법입니다.

browser = webdriver.Chrome()
browser.maximize_window() # 윈도우 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()
#"가는날 선택" 글자를 통해 찾기
# <a href="javascript:;" ng-hide="" role="button" aria-live="polite" aria-label="" ng-class="{txt_trip_on: searchParams['sdate1'] != ''}" ng-click="onClickCalendar('sdate1')" class="txt_trip ng-binding">가는날 선택</a>

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달
  
# 제주도 선택   
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
#<li ng-repeat="city in cities" ng-if="$index < 8" ng-class="$index==0 || $index==6 ? 'recommendation_item_x2' : ''" class="recommendation_item ng-scope recommendation_item_x2">
#xpath 복사해서 붙여넣기 /"recommendationList" -> 'recommendationList' 변경하기  

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
#<a href="javascript:;" role="button" ng-if="tripType!='clearance'" ng-click="searchRealtimeFlights()" class="sp_flight btn_search ng-scope">항공권 검색</a>


try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))  #브라우저를 최대 10초까지 대기하는데 xpath 기준으로 "//*[@id='content']/div[2]/div/div[4]/ul/li[1]" 값에 해당하는 element가 나올때까지 10초동안 기달린다./ 첫번째 결과 xpath 넣어주기
    # 성공했을 때 동작 수행  
    print(elem.text)
finally:        
   browser.quit()   #실패했을때 브라우저 종료

#In the code above, Selenium will wait for a maximum of 10 seconds for an element matching the given criteria to be found. If no element is found in that time, a TimeoutException is thrown. By default, WebDriverWait calls the ExpectedCondition every 500 milliseconds until it returns success. ExpectedCondition will return true (Boolean) in case of success or not null if it fails to locate an element.
#위의 코드에서는 Selenium은 지정된 기준과 일치하는 요소를 찾을 때까지 최대 10 초 기다립니다. 그 시간에 요소가없는 경우 TimeoutException(프로세스나 작업에 할당된 시간이 만료될 때 throw되는 예외)으로 예외처리 됩니다. 기본적으로 WebDriverWait는 성공을 반환 할 때까지 500 밀리 초마다 ExpectedCondition를 호출합니다. ExpectedCondition는 성공했을 경우는 true (부울 값)을 반환 요소의 검색에 실패했을 경우는 null을 반환하지 않습니다.


# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# <li mg-infinite="departure in searchResult.departures" ng-click="selectDeparture(departure)" onclick="nclk(this, 'dsr.schedule')" class="trip_result_item ng-scope"> 
# xpath 복사 후 붙여넣기 

# print(elem.text)

# By (다양한 접근자 존재 NAME, TAG_NAME..)
# WebDriverWait(browser, 10)
# .until
# (EC.presence_of_element_located
#     (
#         (
#             By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"
#         )
#     )
# )


'''
#실행결과
아시아나항공
출발지
GMP
06:05
도착지
CJU
07:10
총 소요시간
01시간 05분
할인석
편도 89,000원
성인
'''