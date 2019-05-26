#! usr/local/bin/python3
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys

def grab_HTML(targetURL): ##get stuff from the website while pretending to be firefox so it works, return a beautifulsoup object with the HTML

	req = Request(targetURL, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, 'lxml')
	return soup ## return

def return_Relevant_SSC_Podcast_Information(htmlInput): ##returns the relevant chunks of information as strings

	body_text_start_index = 22 ++ htmlInput.index("Continue reading →]]>")
	shortBlurb = htmlInput[body_text_start_index:body_text_start_index++512]
	longBlurb = htmlInput[body_text_start_index:body_text_start_index++2500]
	
	title_start_index = htmlInput.index("https://wordpress.org")
	blogTitleChunk = htmlInput[title_start_index:title_start_index++300]
	title_end_index = blogTitleChunk.index('https://slatestarcodex')
	title_start_index = blogTitleChunk.index('\n')
	title = blogTitleChunk[title_start_index:title_end_index]

	return title, shortBlurb, longBlurb

raw_HTML = grab_HTML("https://www.slatestarcodex.com/feed")
plain_text = raw_HTML.text
title, shortBlurb, longBlurb = return_Relevant_SSC_Podcast_Information(plain_text) ## set up variables for printing

sys.stdout = open("descriptions.txt","w") ## print variables to descriptions.txt document
print(title, '\n'*15)
print(shortBlurb, '\n'*15, longBlurb )
sys.stdout.close() 