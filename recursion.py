def cube_list(list):
	i = 0 
	for item in list:
		list[i] = item*item*item
		i += 1

	return list


# print cube_list([2,4,5]) 

def list_reverse(seq):
	if len(seq) == 0:
		return 
	else:
		list_reverse(seq[1:])
		print seq[0],

# list_reverse([1,2,3])


def multiply_list(seq):
	len_of_length = len(seq)
	# even case
	if len_of_length % 2 == 0:

		mid1 = len_of_length / 2
		mid2 = mid1 - 1
		for i in range(len_of_length):
			if not i in [mid1,mid2] :
				seq[i] = seq[i] *(seq[mid2]+seq[mid1])
	# odd case
	else:
		mid = len_of_length/2
		
		for i in range(len_of_length):
			if i != mid :
				seq[i] = seq[i] * seq[mid]
			
	return seq


print multiply_list([2,3,9,11,3,9,11,4,8,9,19,89,3,9,11,4,8,9,1,11,4,8,9,19,89,67,56,89,66,])
