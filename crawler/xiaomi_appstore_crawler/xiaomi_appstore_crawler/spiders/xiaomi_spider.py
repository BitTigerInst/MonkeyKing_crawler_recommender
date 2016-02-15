import scrapy
import re
from scrapy.selector import Selector
from xiaomi_appstore_crawler.items import XiaomiAppstoreCrawlerItem

class XiaomiSpider(scrapy.Spider):
  name = "xiaomi"
  allowed_domains = ["app.mi.com"]

  start_urls = [
    "http://app.mi.com/topList?page=1"
  ]

  def parse(self, response):
    page = Selector(response)

    lis = page.xpath('//ul[@class="applist"]/li')

    url_common = 'http://app.mi.com/'

    for li in lis:
      item = XiaomiAppstoreCrawlerItem()
      item['title'] = li.xpath('./h5/a/text()'). \
          extract_first().encode('utf-8')
      item['url'] = li.xpath('./h5/a/@href').extract_first()
      appid = re.match(r'/detail/(.*)', item['url']).group(1)
      item['appid'] = appid
      item['intro'] = '' # TODO: need to get intro after entering the app detail page
      yield item

      
