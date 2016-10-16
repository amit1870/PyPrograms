from bs4 import BeautifulSoup
import requests, random
from time import sleep
import os

def read_file(file):
	with open(file) as f:
		lines = f.readlines()
	page_content = " ".join(lines)
	soup = BeautifulSoup(page_content,'html5')
	return soup

def get_district(file):
	soup = read_file(file)
	tables = soup.findAll('table', {"class" : "wikitable", "cellspacing": 1, "cellpadding": 1, "border": 0 })
	states = ['AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'CG', 'DN', 'DD', 'DL', 'GA', 'GJ', 'HR',\
			'HP', 'JK', 'JH', 'KA', 'KL', 'LD', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PY',\
			'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UP', 'UK', 'WB']
	i = 0
	data = {}

	for table in tables:
		trs = table.findAll('tr')[1:]
		data[states[i]] = []
		for tr in trs:
			tds = tr.findAll('td')
			try:
				code = str(tds[0].contents[0])
			except:
				code = "NA"

			try:
				district = str(tds[1].findAll('a')[0].contents[0])
			except:
				district = "NA"

			try:
				hq = str(tds[2].findAll('a')[0].contents[0])
			except:
				hq = "NA"

			try:
				population = int(tds[3].contents[0].replace(",",""))
			except:
				population = 0

			try:
				area = int(tds[4].contents[0].replace(",",""))
			except:
				area = 0
			try:
				density = int(tds[5].contents[0].replace(",",""))
			except:
				density = 0

			try:
				url = str(tds[6].findAll('a')[0]['href'])
			except:
				url = "NA"
			data[states[i]].append((code, district, hq, population, area, density, url))
		
		if i == 35:
			break
		
		i += 1
	print data


print get_district("file.html")