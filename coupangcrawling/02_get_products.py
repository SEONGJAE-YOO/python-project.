import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def getPageString(url):
    data = requests.get(url)                       
    return data.content

def getProducts(string):
    bsObj = BeautifulSoup(string,"html.parser")
    ul = bsObj.find("ul",{"id":"productList"})   #<ul id="productList" class="baby-product-list"
    lis = ul.findAll("li")
    print(lis)  
    return []     
     
url = "https://www.coupang.com/np/categories/498704?page=2"
pageString = getPageString(url) 
print(getPageString(pageString))   
         
                 