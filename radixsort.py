# [101,109,108,102,103,108]
def countsort(arr, exp):
	n = len(arr)
	output = [None] * n
	count = [0]*10
	# Store count of occurences in count[]
	for i in range(n):
		# print (arr[i] /exp) % 10,
		count[ (arr[i] /exp) % 10 ] += 1

	# print count
	# Change count[i] so that count[i] now contains actual position of this
	# digit in output[]

	for i in range(1,10):
		count[i] += count[i-1]

	# Build the output array 

	for i in range(n-1,-1,-1):
		output[count[(arr[i] /exp) % 10 ] -1] = arr[i]
		count[(arr[i] /exp) % 10 ] -= 1

	# Copy the output array to arr[], so that arr[] now
	# contains sorted numbers according to current digit

	for i in range(n):
		arr[i] = output[i]
	print arr

def radixsort(arr):
	n = len(arr)
	m = max(arr)
	exp = 1

	while m / exp > 0:
		print m/exp
		countsort(arr,exp)
		exp *= 10

	return arr

print radixsort([111,109,108,102,103,108])




def stringsort(arr):
	maxLen = -1 
	# find longest string 
	for string in arr:
		strlen = len(string)
		if strlen > maxLen: maxLen = strlen 

	buckets = [[]]*26
	for idx in reversed(range(maxLen)):
		for string in arr:
			index = 0 	# assume "empty" character 
			if idx < len(string):	# might be within length 
				index = ord(string[idx]) - 96
			buckets[index].append(string) 
			del arr[:]
			
		for bucket in buckets:
			arr.extend(bucket)
			del bucket[:]
	return arr


arr = ['joe', '', 'bob', 'rot','sue']
print stringsort(arr)



