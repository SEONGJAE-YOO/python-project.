from selenium import webdriver
import time
import random

# chrome webdriver 설정
driver = webdriver.Chrome('C:/Users/MyCom/Downloads/chromedriver_win32 (3)/chromedriver')

# 인스타그램 로그인 정보
insta_id = 'yousong4243@daum.net'
insta_pw = 'tjdwo357'

# 횟수 지정
cycle = 5

# 좋아요반사 = 1, 맞팔 = 2
case_type = 2

# 좋아요 태그
hash_tag_like = '좋아요반사'
# 맞팔 태그
hash_tag_follow = '맞팔'

try:
    # 인스타그램 로그인 페이지 이동
    url_login = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    driver.get(url_login)
    time.sleep(random.uniform(3, 5))

    # 인스타그램 로그인 정보 입력
    id_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_input.send_keys(insta_id)
    password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password_input.send_keys(insta_pw)
    password_input.submit()
    time.sleep(5)

    cnt = 0

    if case_type == 1:
        # 좋아요 cycle 횟수만큼 진행
        while True:
            driver.get("https://www.instagram.com/explore/tags/" + hash_tag_like)
            time.sleep(random.uniform(5, 10))
            element = driver.find_elements_by_class_name("_9AhH0")[9]
            element.click()
            time.sleep(random.uniform(2, 8))

            # 좋아요 반사
            driver.find_element_by_class_name("fr66n").click()

            if cnt == cycle:
                print("좋아요 반사 자동화 종료")
                break
            else:
                print(cnt + 1, "회 좋아요 반사")

            cnt = cnt + 1

    elif case_type == 2:
        # 맞팔 cycle 횟수만큼 진행
        while True:
            driver.get("https://www.instagram.com/explore/tags/" + hash_tag_follow)
            time.sleep(random.uniform(5, 10))
            element = driver.find_elements_by_class_name("_9AhH0")[9]
            element.click()
            time.sleep(random.uniform(2, 8))

            # 맞팔
            driver.find_element_by_class_name("bY2yH").click()

            if cnt == cycle:
                print("맞팔 자동화 종료")
                break
            else:
                print(cnt + 1, "회 맞팔")

            cnt = cnt + 1

    else:
        print("Case is not selected. Check your Case.")

except Exception as e:
    print(e)
finally:
    driver.quit()