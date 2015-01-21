import scraper
import search

file = raw_input("Where do you want to output your results?\n")
query = raw_input("What are you searching for?\n")
for posting in search.getLinks(query):
	scraper.scrapePost(posting, file)