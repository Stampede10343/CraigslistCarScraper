import requests
from lxml import html

def getLinks(input):
	query = input

	url = "http://cleveland.craigslist.org/search/cto?query=" + query
	page = requests.get(url)

	pageTree = html.fromstring(page.text)

	listings = pageTree.xpath("//p[@class='row']")

	allLinks = listings[0].xpath("//a[@class='hdrlnk']/@href")
	linkText = listings[0].xpath("//a[@class='hdrlnk']/text()")

	links = []
	
	for link in  allLinks:
		if not link.startswith("http"):
			link = url[0:url.find("search")-1] + link
			links.append(link)
		else:
			links.append(link)
	
	linkWithText = {}
	linkWithText = dict(zip(linkText, links))

	badLinks = []
	for badLink in linkText:
		if badLink.find(query) == -1 and  badLink.find(query.capitalize()) == -1:
			badLinks.append(badLink)

	for l in badLinks:
		try:
			del linkWithText[l]
		except KeyError:
			pass
	
	return linkWithText.values()

"""
for link in links:
	print i
	if linkText[i].find(query) == -1 or linkText[i].find(query.capitalize()) == -1:
		#print linkText[i] + " Was removed"
		links.remove(link)
		linkText.remove(linkText[i])
		
	if not link.startswith("http"):
		link = url[0:url.find("search")-1] + link
		print linkText[i]
		print link
	else:
		print linkText[i]
		print link
	i+=1
"""