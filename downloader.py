import os
from urllib import urlopen
from os import listdir
from os.path import isfile, join

def download_dl(vcode):
	cwd = os.curdir
	os.chdir(cwd)
	command = "youtube-dl -f 18 https://www.youtube.com/watch?v=%s" % vcode
	print command
	os.system(command)


if __name__ == "__main__":
	status = urlopen("http://www.youtube.com").getcode()
	if status == 200:
		vcodes = ['6ZW6UqJOVgU','IcdRABIYv9E','qRErR62SAH0','BJmkS7azuGU']
		for vcode in vcodes:
			download_dl(vcode)
