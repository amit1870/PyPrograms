import os
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
			if lines != None:

				for line in lines:
					# download video 
					command = " cd ~/Music && youtube-dl -f 18 -q %s" %line
					print command
					os.system(command)
					dlist.append(line)

				for line in dlist:
					lines.remove(line)

			with open(file, 'w') as f:
				if lines == None:
					f.write("")
				else:
					for line in lines:
						f.write(line)
						f.write("\n")
				f.close()

youtube_dl("urls.txt")