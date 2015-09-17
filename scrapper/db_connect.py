from bs4 import BeautifulSoup
import requests, random, MySQLdb
from time import sleep

def connect_db(db, autocommit = True):
    conn  = MySQLdb.connect(host = db[0], # your host, usually localhost
                         user = db[1], # your username
                         passwd = db[2], # your password
                         db = db[3] ) # name of the data base
    
    conn.autocommit(autocommit)
    cur = conn.cursor()
    return cur

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
