def swap(a=10,b=90):
	print a,b
	a = a + b
	print a,b 
	b = a - b
	print a,b
	a = a - b
	return a,b
print swap(10,90)