import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s/ref=lp_283155_nr_p_n_publication_date_0?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&bbn=283155&ie=UTF8&qid=1550908246&rnid=1250225011'
    ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.s-line-clamp-2+ .a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image-fixed-height::attr(src)').extract()

        items['product_name'] = product_name  #items.py 참조
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
		
        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(AmazonSpiderSpider.page_number) + '&fst=as%3Aoff&qid=1617776797&rnid=1250225011&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 75: #amazon page 75페이지가 끝이므로
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse) # page 가 커질수록 parse함수 재호출한다
            