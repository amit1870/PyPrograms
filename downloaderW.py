import os
from urllib import urlopen
from os import listdir
from os.path import isfile, join

Music = os.getcwd()
current_dir = os.getcwd()

def youtube_dl(file):
	# lines = []
	with open(file) as f:
		lines = f.read().splitlines()
		if lines != []:
			lines = map(lambda x : x.strip(), lines)
			if "" in lines:
				lines = lines.remove("")
			f.close()
			
			if lines != None:
				for line in lines:
					# download video
					os.chdir(Music)
					command = "youtube-dl.exe -f 18  https://www.youtube.com/watch?v=%s" %line
					print command
					os.system(command)
			os.chdir(current_dir)

status = urlopen("http://www.youtube.com").getcode()

if status == 200:
	youtube_dl("D:/urls.txt")