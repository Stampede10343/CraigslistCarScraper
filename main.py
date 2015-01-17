import scraper
import search

for posting in search.getLinks("stealth"):
	scraper.scrapePost(posting, "output.html")