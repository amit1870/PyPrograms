def counting_sort(A,k):
	# creating a temp array for counting values in the range k 
	C = [0]*(k+1)
	B = [None] * len(A)
	len_A = len(A)
	 
	for x in range(0,len_A):
		C[A[x]] = C[A[x]] + 1
	# C[i] now contains the number of elements equal to i 
	print C
	
	for y in range(0,k+1):
		C[y] = C[y] + C[y-1]

	# C[i] now contains the number of elements less than or equal to i 

	print C
	# putting A[j] into its correct sorted postion in B
	for j in range(len_A-1,-1,-1):
		print C[A[j]],
		B[C[A[j]]-1] = A[j]
		C[A[j]]  = C[A[j]] - 1
		print C

	return B

A = [2,1,3,0,1,1,2,3,0,1]


print counting_sort(A,5)
