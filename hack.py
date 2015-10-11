def XaeroBday(A,B):
	if len(A) != len(B):
		return -1 
	if A.count('1')  != B.count('1'):
		return -1

	A = list(A)
	B = list(B)
	i = 0
	count = 0
	while i < len(B):
		if A[i] != B[i]:
			for k in range(i+1,len(B)):
				if A[k] != B[k]:
					break
			temp = B[k]
			B[k] = B[i]
			B[i] = temp
			i = k+1
			count += 1
		else:
			i += 1
	return count

# A = raw_input()
# B = raw_input()

# print XaeroBday('1001101111101011011100101100100110111011111011000100111100111110111101011011011100111001100011111010','1001101111101011011100100011100110111011111011000100111100111110111101011011011100111001100011111100')

