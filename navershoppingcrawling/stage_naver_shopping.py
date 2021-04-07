from crawler import crawl
from parserr import parse

pageString = crawl('')
products = parse(pageString)
print(products)
#6분 23초 /https://www.youtube.com/watch?v=fz9RQgERfhs&list=PLAdQRRy4vtQRzdg7D9n1rkDp9DIeWpBQ9&index=48
