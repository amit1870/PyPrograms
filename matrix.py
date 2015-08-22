def matrix_multiply(A,B):
	rowsA = len(A)
	rowsB = len(B[0])

	if len(A[0]) != len(B):
		return

	matrixC = [ [None for y in range(rowsB)]  for x in range(rowsA)]
	
	for i in range(rowsA):
		for j in range(rowsB):
			matrixC[i][j] = 0
			for k in range(rowsB):
				matrixC[i][j] = matrixC[i][j] + A[i][k]*B[k][j]
	return matrixC

def create_matrix(row,col):
	return [ [x+y+col for y in range(col)] for x in range(row)]


A = create_matrix(300,50)
B = create_matrix(50,30)
print A
print B

print matrix_multiply(A,B)



