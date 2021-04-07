import scrapy
from ..items import TutorialItem

class  QuoteSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2
    start_urls = {
        'http://quotes.toscrape.com/page/1/'
    } 
#<title>Quotes to Scrape</title>
    def parse(self,response):  #Parse -> Analyse (a string or text) into logical syntactic components.
        # title = response.css('title::text').extract()
        # yield {'titletext': title} #Yield는 함수가 제너레이터를 반환한다는 것을 제외하고 return과 비슷하게 사용되는 키워드
        items = TutorialItem()

        all_div_quotes = response.css('div.quote') #<div class="quote"
         
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()  #<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
            author = quotes.css('.author::text').extract()#<small class="author" itemprop="author">Albert Einstein</small>
            tag = quotes.css('.tag::text').extract() #<a class="tag" href="/tag/change/page/1/">change</a>
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items

        next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) +  '/'  # QuoteSpider클래스 이름 넣기

        #다음 페이지가 없을때 
        
        if QuoteSpider.page_number < 11: #page가 10페이지 밖에 없으므로
           QuoteSpider.page_number += 1
           yield response.follow(next_page, callback= self.parse)  #내가 함수를 호출하는 것이 아니라 다른 함수에서 호출하는 것: 콜백함수(callback)





