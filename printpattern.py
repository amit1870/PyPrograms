def print_pattern(n):
	k = 0
	for i in range(1,n+1):
		for j in range(1,i+1):
			print k+j,
		k += 1
		print 


print_pattern(5)