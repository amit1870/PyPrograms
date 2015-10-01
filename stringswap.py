def XaeroBday(A,B):
	if len(A) != len(B):
		return -1 

	if A.count('1') != B.count('1'):
		return -1
	A = list(A)
	B = list(B)
	# scan B 
	j = 1
	count = 0
	for i in range(0,len(B)):
		if A[i] != B[i]:
			for k in range(j,len(B)):
				if A[k] != B[k]:
					temp = B[k]
					B[k] = B[i]
					B[i] = temp
			count += 1
			j = i
	return count


A = raw_input()
B = raw_input()
print XaeroBday(A,B)


