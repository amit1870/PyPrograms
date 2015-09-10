def partition(seq,low,high):
	pivot = seq[high]
	i = low - 1
	for j in range(low, high):
		if seq[j] <= pivot:
			i += 1
			swap(seq,i,j)

	swap(seq,i+1,high)
	print seq
	return i+1


def quicksort(seq,low,high):
	if low < high:
		p = partition(seq,low,high)
		quicksort(seq,low,p-1)
		quicksort(seq,p+1,high)

	return seq

def swap(seq,i,j):
	tmp = seq[i]
	seq[i] = seq[j]
	seq[j] = tmp

seq = [34,34,34,34,34,34,34]
print quicksort(seq,0,len(seq)-1)