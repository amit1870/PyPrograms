import sys

def convertToList(file,outout):
	with open(file) as f:
		lines = [line.rstrip('\n') for line in f]

	with open(outout,'a') as f:
		f.write(str(lines))


convertToList(sys.argv[1],sys.argv[2])