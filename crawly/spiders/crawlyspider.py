from scrapy.spiders import Spider
from scrapy.http    import Request
from scrapy import stats
from crawly.items   import CrawlyItem
from urlparse import urljoin

class MySpider(Spider):
    name = "crawly"
    allowed_domains = ["token.wfk.io"]
    start_urls = ["http://token.wfk.io"]

    def parse(self, response):
        links = response.xpath("//a/@href").extract()
        crawledLinks = []

        print "* URL ", response.url
        for link in links:
            #final_url = urllib2.urlopen(link, None, 1).geturl()
            #print "***URL", final_url
            print "* Link ", link
            l = urljoin(response.url, link) 
            if not l  in crawledLinks:
                crawledLinks.append(l)
                #https://doc.scrapy.org/en/latest/topics/request-response.html#scrapy.http.Request
                priority = 1 if "honey" in link else -1
                yield Request(l, self.parse, priority=priority)

        titles = response.xpath("//a/text()").extract()
        for title in titles:
            item = CrawlyItem()
            item["title"] = title
            yield item

    def closed(self, reason):
        print "Here are the stats"
        print stats.get_stats()
