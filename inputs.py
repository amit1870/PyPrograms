inputs = raw_input()
M,N,R = map(initit,inputs.split(" "))
temp = M
matrix = []
while temp > 0 :
	row = raw_input()
	row = map(initit, row.split(" "))
	matrix.append(row)
	temp -= 1


# input for grid pattern 
T = input()
G = []
P = []
while T > 0:
	ins = raw_input()
	R,C = map(initit,ins.split(" "))
	while R > 0:
		cols = raw_input()
		column = []
		for x in cols:
			column.append(int(x))
		G.append(column)
		R -= 1

	ins = raw_input()
	r,c = map(initit,ins.split(" "))
	while r > 0:
		cols = raw_input()
		column = []
		for x in cols:
			column.append(int(x))
		P.append(column)

		r -= 1

	print gridPattern(G,P)
	T -= 1
