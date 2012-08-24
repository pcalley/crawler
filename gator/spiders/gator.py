from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.item import Item, Field 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time
import pprint

class GatorItem(Item):
    url = Field()
    title = Field()
    thatDiv = Field() 


class GatorSpider(CrawlSpider):
    name = "gator"
    start_urls = ["http://localhost:3000"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('\.html', ), allow_domains=('localhost:3000', )), callback='parse_page',follow=True),
    )

    def __init__(self):
        CrawlSpider.__init__(self)
        self.verificationErrors = []
        #create a profile with specific add-ons
        #and do this. Firefox to load it
        profile = FirefoxProfile(profile_directory="/Library/Python/2.6/site-packages/selenium/webdriver/firefox")
        self.selenium = webdriver.Firefox(profile)

    def __del__(self):
        self.selenium.quit()
        print self.verificationErrors
        CrawlSpider.__del__(self)

    def parse_page(self, response):
        #normal scrapy result
        hxs = HtmlXPathSelector(response)
        #webdriver rendered page
        sel = self.selenium
        sel.get(response.url)

        if sel:
            #Wait for javascript to load in Selenium                                                                                       
            time.sleep(2.5)

        #Do some crawling of javascript created content with Selenium                                                                      
        item = GatorItem()
        item['url'] = response.url
        item['title'] = hxs.select('//title/text()').extract()

