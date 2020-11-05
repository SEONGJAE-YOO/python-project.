import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)  
pageObj = requests.get(url)
soup = BeautifulSoup(pageObj.text,"lxml")   

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
#print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    # f.write(soup.prettify()) # html 문서를 예쁘게 출력
   
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)