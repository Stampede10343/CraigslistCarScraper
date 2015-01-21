from lxml import html
from lxml import etree
import requests

def scrapePost(url, outputFile):
	output = open(outputFile, "a")
	
	page = requests.get(url)
	tree = html.fromstring(page.text)

	body = tree.xpath('//section[@id="postingbody"]/text()')

	titleArr = tree.xpath('//h2[@class="postingtitle"]/text()')
	
	#images = tree.xpath('/html/body/article/section/section[2]/figure/div[2]/div')
	try:
		noImages = False
		images = tree.xpath('//div[@class="tray"]')
		imgurls = images[0].xpath('//img["@source="]')

	except IndexError:
		print "No images"
		noImages = True

	title = titleArr[1]
	
	title = title.lstrip()
	print title
	print url
	
	output.write("<header>")
	output.write("<h3>" + title.title() + "</h3>")
	output.write("<h4>" + '<a href="' + url + '">link</a>' + "</h4>")
	output.write("</header>" )

	for line in body:
		if line == "\n":
			continue
		line.lstrip(line)
			
		#line.replace("  ", " ")
		print line.lstrip()
		
		output.write("<p style= width: 400px>")
		output.write(line.lstrip())
		output.write("</p>")
	
	#print imgurls
	
	#for img in imgurls:
		#print img.attrib['src']
	if not noImages:
		print images[0].xpath('//img/@src')[0]
		output.write('<img src="')
		output.write(images[0].xpath('//img/@src')[0].lstrip() + '"')
		output.write(' alt="image" >')
	
	output.write("<br><br><br>")
	output.close()
	
	return
		
#scrapePost("http://cleveland.craigslist.org/cto/4845829986.html")