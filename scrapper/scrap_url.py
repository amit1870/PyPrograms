from bs4 import BeautifulSoup, element
import db_connect as db
import re, requests, random
import time

def scrap_url(main_url,source,city,category,page_id, cur):
	url = main_url + "/" + city + "/" + category + "/page-" + str(page_id)
	soup = db.read_url(url)
	# print soup
	jbbgs = soup.findAll('section', {"class" : "jbbg" })
	jgbgs = soup.findAll('section', {"class" : "jgbg" })

	items = jbbgs + jgbgs
	if(len(items)==0):
		return False

	for jcar in items :
		info = {'name':'', 'key':'', 'city':'', 'addr':'', 'tags':'','numbers':'','category':'','content':''}
		soup_name = jcar.findAll('span',{'class','jcn'})[0].findAll('a')[0]
		
		info['name'] = soup_name.contents[0]
		info['city'] = city
		info['category'] = category
		
		link = soup_name['href']

		try:
			info['key'] = link[link.rfind('/')+1:-(len(link)-link.find('_'))]
		except:
			info['key'] = 'NA'

		try:
			soup_number = jcar.findAll('p',{'class','jrcw'})[0].findAll('a')
			numbers = []
			for number in soup_number:
				numbers.append(number.contents[0])
			info['numbers'] = ",".join(numbers)
		except:
			info['numbers'] = 'NA'

		try:
			soup_addr = jcar.findAll('p',{'class','jaid'})[0]
			info['addr'] = soup_addr.contents[1]
		except:
			info['addr'] = 'NA'

		try:
			soup_tags = jcar.findAll('p',{'class','fcatname'})[0].contents
			tags = []
			for tag in soup_tags:
				if(not isinstance(tag,element.NavigableString)):
					tags.append(tag.contents[0].strip())
			info['tags'] = ",".join(tags)
		except:
			info['tags'] = "NA"
        
		info = {k: db.MySQLdb.escape_string(v.encode('ascii', 'ignore')) for k, v in info.items()}
		sql = "INSERT INTO contctus_listing (`source`, `city`, `name`, `category`, `numbers`,`addr`, `tags`, `key`,`content`,`link`) \
				VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (source,info['city'],info['name'],info['category'],\
				info['numbers'],info['addr'],info['tags'],info['key'],info['content'],link)
		# print sql
		cur.execute(sql)
		inserted_id = str(cur.lastrowid)
		print inserted_id
	return True
		
