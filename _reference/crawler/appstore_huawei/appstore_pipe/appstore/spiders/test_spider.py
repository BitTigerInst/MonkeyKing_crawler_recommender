import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule

class TestSpider(scrapy.Spider):
  name = "test1"
  allowed_domains = ["appstore.huawei/.com"]
  # start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"]
  start_urls = ["http://appstore.huawei.com/more/all"]
  
  rules = (
    Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="page-ctrl ctrl-app"]/a')), callback="parse", follow=True,),
  )

  def start_requests(self):
    for url in self.start_urls:
      yield scrapy.Request(url, self.parse, meta={
        'splash': {
          'endpoint': 'render.html',
          'args': {'wait': 0.5}
        }
      })

  def parse(self, response):
    print "QQQQQ", response
