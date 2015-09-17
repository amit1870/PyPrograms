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
# print maximum_subarray(A,0,len(A)-1)


def cross_maximum_subarray_linear(A):
	max_so_far = 0 
	max_ending_here = 0
	array = []
	for item in A:
		max_ending_here += item
		if max_ending_here < 0 :
			max_ending_here = 0

		if max_ending_here > max_so_far:
			max_so_far = max_ending_here
			array.append(item)

	return max_so_far,array
	
# print cross_maximum_subarray_linear(A)


rev_num = 0
base_pos = 1
def reverseDigit(number):

	"""
	python(global) == C(static) 
	Concept: A static variable inside a function keeps its value between invocations.

	http://stackoverflow.com/questions/572547/what-does-static-mean-in-a-c-program
	"""
	global rev_num, base_pos

	if number > 0:
		reverseDigit(number / 10)
		rev_num += (number % 10 )* base_pos
		base_pos *= 10

	return rev_num

def pallindrom(number):
	''' this program print trailing 0's in reverse number '''

	zeros = 0 
	while number:
		if number % 10 == 0:
			zeros += 1
			number /= 10
		else:
			break

	print "%s%s" % ("0"*zeros, reverseDigit(number))

	if reverseDigit(number) == number:
		return "Pallindrom"
	else:
		return "Not Pallindrom"

print pallindrom(10000010)
