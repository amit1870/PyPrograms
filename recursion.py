def insertion_sort(A):
	
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key

	return A

A = [2,1,18,2,1,18,9,2,1,18,9,9,2,18,9,2,1,18,9,9,2,1,18,9,2,1,18,9,3,989,90,78,56,45,34,2,-1,-10,90,-90,	]

# print insertion_sort(A)

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

def bianry_search(seq,key,low,high):
	# using recusion to search an element in bianry search 
	if low <= high:
		mid = (low+high) / 2
		if seq[mid] == key:
			return mid
		elif seq[mid] > key:
			return bianry_search(seq,key,low,mid-1)
		else:
			return bianry_search(seq,key,mid+1,high)
	
	return None

	# using iteration return index of found element 
	

	while low <= high :
		mid = (low+high) / 2
		if seq[mid] == key:
			return mid
		elif seq[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
	return None


seq = [2,4,6,7,8,10,23]
key = 6 
low = 0
high = len(seq) - 1

# print bianry_search(seq,key,low,high)


def list_reverse(seq):
	if len(seq) == 0:
		return 
	else:
		list_reverse(seq[1:])
		print seq[0],

# list_reverse([1,2,3])


def maximum_subarray(A,low,high):
	if high == low:
		return (low,high,A[low])
	else:
		mid = (low+high)/2

		(left_low, left_high, left_sum) = maximum_subarray(A,low,mid)
		(right_low, right_high, right_sum) = maximum_subarray(A,mid+1,high)
		(cross_low, cross_high, cross_sum) = cross_maximum_subarray(A,low,mid,high)

		if left_sum > right_sum and left_sum > cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum > left_sum and right_sum > cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)



def cross_maximum_subarray(A,low,mid,high):
	left_sum = -9000
	sum = 0
	max_left = None
	for x in range(mid,low,-1):
		sum = sum + A[x]
		if sum > left_sum:
			left_sum = sum
			max_left = x

	right_sum = None
	max_right = -1900
	sum = 0 
	for x in range(mid+1,high+1):
		sum = sum + A[x]
		if sum > right_sum:
			right_sum = sum
			max_right = x

	return (max_left, max_right, left_sum + right_sum)

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print maximum_subarray(A,0,len(A)-1)


def cross_maximum_subarray_linear(A):
	pass

print cross_maximum_subarray_linear(A)

def heapsort(A):
	

