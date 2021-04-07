#login.py 실행 시키는법
#파일명을 quotes_spider.py로 변경해서 터미널에서 scrapy crawl quotes 입력

import scrapy
from scrapy.http import FormRequest #formdata를 사용할때 필수임
from scrapy.utils.response import open_in_browser
from ..items import TutorialItem

class  QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = {
        'http://quotes.toscrape.com/login'
    } 
#<title>Quotes to Scrape</title>
    def parse(self,response):  #Parse -> Analyse (a string or text) into logical syntactic components.
        token = response.css('form input::attr(value)').extract_first()   #<input type="hidden" name="csrf_token" value="WolIbkyQEjPZwcritfnCKFADReaMSXLsHghYUmVuxzpJTOvdBGqN">
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'yousong4243@naver.com',
            'password' : '1234'
        },callback=self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
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

     
