# parser(문자열에서 데이터 뽑기)
from bs4 import BeautifulSoup

def parse(pageString):

    bsObj = BeautifulSoup(pageString,"html.parser")
    ul = bsObj.find("ul",{"class":"list_basis"})

    print(ul)
    return []  