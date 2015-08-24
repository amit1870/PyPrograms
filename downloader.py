import os
from urllib import urlopen
def youtube_dl(file):
	# lines = []
	with open(file) as f:
		lines = f.read().splitlines()
		if lines != []:
			lines = map(lambda x : x.strip(), lines)
			if "" in lines:
				lines = lines.remove("")
			f.close()
			dlist = []
			current_dir = os.getcwd()
			Music = "/home/amit/Music"
			if lines != None:
				for line in lines:
					# download video
					os.chdir(Music)
					command = "youtube-dl -f 18 -q %s" %line
					print command
					os.system(command)
					dlist.append(line)

				for line in dlist:
					lines.remove(line)
			os.chdir(current_dir)
			with open(file, 'w') as f:
				if lines == None:
					f.write("")
				else:
					for line in lines:
						f.write(line)
						f.write("\n")
				f.close()

status = urlopen("http://www.youtube.com").getcode()

if status == 200:
	youtube_dl("urls.txt")