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

  url_id = 1

  def parse(self, response):
    page = Selector(response)

    lis = page.xpath('//ul[@class="applist"]/li')
    if lis == None:
      return

    url_common = 'http://app.mi.com/'

    for li in lis:
      item = XiaomiAppstoreCrawlerItem()
      item['title'] = li.xpath('./h5/a/text()'). \
          extract_first().encode('utf-8')
      url = li.xpath('./h5/a/@href').extract_first()
      appid = re.match(r'/detail/(.*)', url).group(1)
      item['appid'] = appid
      item['intro'] = '' # TODO: need to get intro after entering the app detail page
      item['recommended'] = ''
      yield item

    import pudb; pu.db
    url_id = re.match(r'page=(.*)', response.url).group(1) 
    url_common2 = 'http://app.mi.com/topList?page='
    url_next = url_common2 + str(int(url_id) + 1)    
    yield scrapy.Request(url_next, callback=self.parse)
