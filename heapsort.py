def heapsort(seq,heap_type=1):
	length = len(seq)-1
	if heap_type:
		build_max_heap(seq,length)
		for i in range(length,0,-1):
			swap(seq,0,i)
			max_heapify(seq,0,i-1)
	else:
		build_min_heap(seq,length)
		for i in range(length,0,-1):
			swap(seq,0,i)
			min_heapify(seq,0,i-1)

	return seq

def build_max_heap(seq,length):
	leastParent = length/2
	for i in range(leastParent,-1,-1):
		max_heapify(seq,i,length)


def build_min_heap(seq, length):
	maxParent = length/2
	for i in range(maxParent,-1,-1):
		min_heapify(seq,i,length)

def min_heapify(seq,i,length):
	left = 2*i + 1
	right = 2*i + 2
	if left <= length and seq[left] < seq[i]:
		minimum = left
	else:
		minimum = i
	if right <= length and seq[right] < seq[minimum]:
		minimum = right
	if minimum != i:
		swap(seq,i,minimum)
		min_heapify(seq,minimum,length)
	else:
		return


def max_heapify(seq,i,length):
	# iterative version
	largest = 2 * i + 1
	while largest <= length:
		# right child exists and is larger than left child 
		if largest < length and seq[largest] < seq[largest+1]:
			largest += 1

		if seq[largest] > seq[i]:
			swap(seq,largest,i)
			# move down to largest child 
			i = largest
			largest = 2 * i + 1
		else:
			return

	# recursive procedure
	left = 2*i + 1
	right = 2*i + 2
	if left <= length and seq[left] > seq[i]:
		largest = left
	else:
		largest = i
	if right <= length and seq[right] > seq[largest]:
		largest = right
	if largest != i:
		swap(seq,i,largest)
		max_heapify(seq,largest,length)
	else:
		return

def swap(seq,i,j):
	tmp = seq[i]
	seq[i] = seq[j]
	seq[j] = tmp

seq = [3,45,5,65,6,7,8]
print heapsort(seq,heap_type=1)