sum = 0 
def sum_array(arr):
	global sum
	if arr == []:
		return 
	else:
		sum_array(arr[:-1])
		sum = sum + arr[-1]
	return sum


def sum_list(arr):
	sum = 0 
	for item in arr:
		sum += item
	return sum