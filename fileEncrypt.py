from sys import argv


def encrypt_file(file,key=None):
	content = open(file)
	# print content.read()
	text = content.read()
	content.close()
	lines = text.splitlines()

	for line in lines:
		list_line = list(line)
		

			
			






# script, filename = argv
filename = "urls.txt"
encrypt_file(filename)
