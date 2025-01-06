import scrapy
from urllib.parse import urlencode
from amazon_scraper.items import AmazonScraperItem
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_scrapeops_url(url):
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    #allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in"]

    def start_requests(self):
        keyword=['pendrive']

        for word in keyword:
            for page in range(1,10):
                url=f'https://www.amazon.in/s?k={word}&page={page}'
                yield scrapy.Request(get_scrapeops_url(url))
    
    
    
    def parse(self, response):
        products=response.xpath('//a[@class="a-link-normal s-line-clamp-2 s-link-style a-text-normal"]/@href').getall()
        for product in products:
            product_url='https://www.amazon.in'+product
            yield response.follow(get_scrapeops_url(product_url),callback=self.parse_product)

    def parse_product(self,response):
       object = AmazonScraperItem()
       
       object['name']=response.xpath('//span[@class="a-size-large product-title-word-break"]/text()').get()
       object['price']=response.xpath('//span[@class="a-price-whole"]/text()').get()
       object['brand']=response.xpath('//span[@class="a-size-base po-break-word"]/text()').get()
       object['memory_storage_capacity']=response.xpath('//tr[@class="a-spacing-small po-memory_storage_capacity"]//td[@class="a-span9"]//span/text()').get()
       object['hardware_interface']= response.xpath('//tr[@class="a-spacing-small po-hardware_interface"]//td[@class="a-span9"]//span/text()').get()
       object['features']= response.xpath('//tr[@class="a-spacing-small po-special_feature"]//td[@class="a-span9"]//span/text()').get()
       object['write_speed']=response.xpath('//tr[@class="a-spacing-small po-write_speed"]//td[@class="a-span9"]//span/text()').get()

       yield object