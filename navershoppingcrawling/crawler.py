import requests
# crawler(url로 문자열 받아오기)
def crawl(keyword):
    url="https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=숨셔바요"
    data = requests.get(url)
    print(data.status_code,url)
    return data.content

