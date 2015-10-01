A = [2,1,18,2,1,18,9,2,1,18,9,9,2,18,9,2,1,18,9,9,2,1,18,9,2,1,18,9,3,989,90,78,56,45,34,2,-1,-10,90,-90,]

# using insertion sort in which card insertion play a important role
# we pick one card from pile and put it in hand in sorted manner
# when we pick the next card from pile, we compare this card with all 
# and insert into its final postion. So every time cards will be sorted.

def insertion_sort(A):
	
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key

	return A

print insertion_sort(A)

# merge sort use divide and conquer algorithm
# this divides the input array to non-dividable chunk of element (one element)
# one element in list is always sorted,now we meger them recusively to form a 
# new array with sorted data.

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    else:
        #recursion: break sequence down into chunks of 1
        mid = len(seq)/2
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])

        i, j, k = 0, 0, 0 #i= left counter, j= right counter, k= master counter

        #run until left or right is out
        while i < len(left) and j < len(right):
            #if current left val is < current right val; assign to master list
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1; k += 1
            #else assign right to master
            else:
                seq[k] = right[j]
                j += 1; k += 1

        #handle remaining items in remaining list
        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            seq[k] = remaining[r]
            r += 1; k += 1

        return seq

# print merge_sort(A)

# quick sort is a comparison and in place sorting like insertion sort 
# this algo works on choosing the pivot element. Pick the last element as 
# the pivot element and move the greater element to right of this and smaller
# to left of this element. And put this pivot element into final postion when
# array will be sorted.

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
# print quicksort(seq,0,len(seq)-1)
