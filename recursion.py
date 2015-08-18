def cube_list(list):
	i = 0 
	for item in list:
		list[i] = item*item*item
		i += 1

	return list


print cube_list([2,4,5]) 

def list_reverse(seq):
	if len(seq) == 0:
		return 
	else:
		list_reverse(seq[1:])
		print seq[0],

list_reverse([1,2,3])