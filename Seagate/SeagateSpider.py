from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector

# Constants
first = '?sku='
last = '&'
duplicate_part = []

def find_between( s, first, last ):
	start = s.index( first ) + len( first )
	end = s.index( last, start )
	return s[start:end]

class SeagateSpider(SitemapSpider):
	name = 'seagate'
	sitemap_urls = ['http://www.seagate.com/sitemap1.xml.gz','http://www.seagate.com/sitemap2.xml.gz','http://www.seagate.com/sitemap3.xml.gz','http://www.seagate.com/sitemap4.xml.gz','http://www.seagate.com/sitemap5.xml.gz','http://www.seagate.com/sitemap6.xml.gz']
	#sitemap_urls = ['http://www.seagate.com/sitemapindex.xml']
	sitemap_rules = [('/support/','parse_pdf')]

	def parse_pdf(self, response):
		duplicate_link = []
		links = response.selector.xpath('//a/@href').extract()
		s = find_between(response.url,first,last)
		for link in links:
			if '.pdf' in link and '/www-content/' in link:
				if link not in duplicate_link and s not in duplicate_part:
					duplicate_link.append(link)
					with open('Seagate.txt', 'a') as f:
						f.write(link + '\t' + s + '\n')
		duplicate_part.append(s)