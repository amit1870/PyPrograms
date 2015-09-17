import config
import db_connect as db
from scrap_url import scrap_url

cur = db.connect_db( config.db )

for city in config.cities:	
	for category in config.categories:		
		print "********** Scrapping for %s - %s **************\n" % (city,category)
		more_pages = True
		#sql = "DELETE FROM `contctus_listing` WHERE source = '%s' AND city = '%s' AND category = '%s'" % (config.source,city,category)
		# print sql 
		#cur.execute(sql)
		i=1
		while(more_pages):
			print "_________ Page %d \n" % i
			more_pages = scrap_url(config.main_url,config.source,city,category,i,cur)
			print "_________ More Pages %s \n" % str(more_pages)
			i+=1

		sql = "SELECT id FROM scrapper_log WHERE source ='%s' and city='%s' and category='%s' " %(config.source,city,category)
		result = cur.execute(sql) 
		if not cur.fetchone() :
			sql = "INSERT INTO `scrapper_log`(source,city,category,status,update_time)  VALUES ('%s','%s','%s','scrapped',now())" % (config.source,city,category)
		else :
			sql = "UPDATE `scrapper_log` SET status='scrapped', update_time = now() WHERE source ='%s' and city='%s' and category ='%s' " %(config.source,city,category)

		cur.execute(sql) 


print "********** Scrapping Done **************\n"


