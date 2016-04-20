from bs4 import BeautifulSoup
import requests, random
from time import sleep
import urllib
import os

def read_url(url, format='soup'):
    sleep(random.randint(1,3))
    headers = {'Accept':'text/css,*/*;q=0.1',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'en-US,en;q=0.8',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'}
    page = requests.get(url, headers = headers)
    page_content = page.content

    soup = BeautifulSoup(page_content,'html5')
    if(format=='str'):
        return str(soup)
    else:
        return soup

def download_rajiv_bhai_audio(main_url,category):
	url = main_url + category
	print url
	soup = read_url(url)
	blockquotes = soup.findAll('blockquote')
	for blockquote in blockquotes:
		link = blockquote.findAll('a')[0]['href']
		soup = read_url(link)
		div = soup.findAll('div', {"class" : "entry" })[0].findAll('blockquote')[0].findAll('a')[1]
		href = div['href']
		soup = read_url(href)
		download = soup.findAll('center')[-1].findAll('a')[0]['href']
		print download

		os.chdir("/home/amit/Downloads")
		os.system ("wget %s" % download)

main_url = "http://www.rajivdixitmp3.com/"
categories = ["bharat-ki-aajadi-ya-dhokha18-lectures/","health-lecture-swasthya-katha-sabhi-bimariyo-ka-samadhan18-lectures/",\
			"organic-farmingjavik-kheti-lecture-aur-gau-raksha13-lectures/","wto-agreement-globalisation-indian-economy-collapse27-lectures/",\
			"bharat-vs-europe-sabhyta-aur-sanskriti/","kargil-yudh-aur-kashmir-ki-samsya/","lecturen-during-bharat-swabhiman-andolan/",\
			"ram-katha-mein-bhart-ki-samsyao-ka-samadhan/","lecture_for_volunteer_workers/","othres-important-lectures/"]

for category in categories:
	download_rajiv_bhai_audio(main_url,category)
	
