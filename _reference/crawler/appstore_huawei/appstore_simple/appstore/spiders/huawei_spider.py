import scrapy
import re
from scrapy.selector import Selector
from appstore.items import AppstoreItem

class HuaweiSpider(scrapy.Spider):
  name = "huawei"
  allowed_domains = ["huawei.com"]

  start_urls = [
    "http://appstore.huawei.com/more/all"
  ]

  def parse(self, response):
    page = Selector(response)

    divs = page.xpath('//div[@class="game-info  whole"]')

    for div in divs:
      item = AppstoreItem()
      item['title'] = div.xpath('.//h4[@class="title"]/a/text()'). \
          extract_first().encode('utf-8')
      item['url'] = div.xpath('.//h4[@class="title"]/a/@href').extract_first()
      appid = re.match(r'http://.*/(.*)', item['url']).group(1)
      item['appid'] = appid
      item['intro'] = div.xpath('.//p[@class="content"]/text()'). \
          extract_first().encode('utf-8')
      yield item

      
