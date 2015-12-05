from bs4 import BeautifulSoup, element
import re, requests, random
from time import sleep
import socket

main_url = 'http://sec.up.nic.in/ElecLive/SearchReservationOnPost.aspx'


def read_url(url, format='soup'):
    sleep(random.randint(3,6))
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

def scrape_url(url):
	soup = read_url(url)
	print soup

socket.create_connection((main_url, 8181), timeout=2)

# scrape_url(main_url)