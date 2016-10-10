import os
from urllib import urlopen
from os import listdir
from os.path import isfile, join

def download_dl(vcode):
	cwd = os.curdir
	os.chdir(cwd)
	if os.environ['OS'] == "WINDOWS_NT":
		command = "youtube-dl.exe -f 18 https://www.youtube.com/watch?v=%s" % vcode
	else:
		command = "youtube-dl -f 18 https://www.youtube.com/watch?v=%s" % vcode
	print command
	os.system(command)




if __name__ == "__main__":
	status = urlopen("http://www.youtube.com").getcode()
	if status == 200:
		vcodes = ['tTFr78q0lXM',]
		for vcode in vcodes:
			download_dl(vcode)
