from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector

# Constants
first = '?sku='
last = '&'
duplicate_part = []

def find_between( s, first, last ):
	if last in s:
		start = s.index( first ) + len( first )
		end = s.index( last, start )
	else:
		start = s.index( first ) + len( first )
		end = len(s)-1
	return s[start:end]

class SeagateSpider(CrawlSpider):
	name = 'seagateStart'
	with open('/home/feardameow/scraper/Seagate/Seagate/spiders/2.txt') as f:
		start_urls = [url.strip() for url in f.readlines()]

	def parse(self, response):
		duplicate_link = []
		links = response.selector.xpath('//a/@href').extract()
		s = find_between(response.url,first,last)
		for link in links:
			if '.pdf' in link and '/www-content/' in link:
				if link not in duplicate_link and s not in duplicate_part:
					duplicate_link.append(link)
					with open('/home/feardameow/scraper/Seagate/Seagate/Seagate.txt', 'a') as f:
						f.write(link + '\t' + s + '\n')
		duplicate_part.append(s)