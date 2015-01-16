from lxml import html
from lxml import etree
import requests

def scrapePost(url):

	page = requests.get(url)
	tree = html.fromstring(page.text)

	body = tree.xpath('//section[@id="postingbody"]/text()')

	titleArr = tree.xpath('//h2[@class="postingtitle"]/text()')
	
	#images = tree.xpath('/html/body/article/section/section[2]/figure/div[2]/div')
	images = tree.xpath('//div[@class="tray"]')

	title = titleArr[1]
	
	title = title.lstrip()
	print title

	for line in body:
		if line == "\n":
			continue
		line.lstrip(line)
			
		#line.replace("  ", " ")
		print line.lstrip()
	
	imgurls = images[0].xpath('//img["@source="]')
	
	#print imgurls
	
	#for img in imgurls:
		#print img.attrib['src']
	
	print images[0].xpath('//img/@src')[0]
		
scrapePost("http://cleveland.craigslist.org/cto/4845829986.html")