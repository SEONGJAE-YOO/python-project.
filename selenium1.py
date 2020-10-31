# from selenium import webdriver     
# from webdriver_manager.chrome import ChromeDriverManager   #pip install webdriver-manager 으로 설치해줌

# driver = webdriver.Chrome(ChromeDriverManager().install()) 

import requests

url = 'http://news.khan.co.kr/kh_news/khan_art_view.html?art_id=201707111831001'
req = requests.get(url)
print(req.content.decode('utf-8'))
   