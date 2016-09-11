#Jacob Pawlak
#Maybe it's a web scraper?
#Start date October 19th, 2015
#Note - Download the BeautifulSoup Library AFAP

'''
Scrape for sports data for like fantasy football
can create an algorithm that would rate players based on scraped data

www.rotogrinders.com - possible scrape page. 
'''

from urllib import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")
	beautifulObj = BeautifulSoup(html.read())
	print(beautifulObj.h1)
	print("This is the <h1> tag from pythonscraping.com/pages/page1")

	
	try:
		html2 = urlopen("http://reddit.com/r/programmerhumor")
		beautifulObj2 = BeautifulSoup(html2.read())
		print(beautifulObj2.p)
		if(html2.read()):
			print("read")
		else:
			print("Not read")
	except (ValueError, urllib.error.HTTPError) as e:
		print("This should be the reddit.com/r/programminghumor <p> tags")
		print(e.args)

main()
