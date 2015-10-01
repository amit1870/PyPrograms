def swap(string,l,r):
	temp = string[l]
	string[l] = string[r]
	string[r] = temp

def permute(string,left,right):
	if left == right:
		print "".join(string)

	else:
		for i in range(left,right+1):
			swap(string,left,i)
			permute(string,left+1,right)
			swap(string,left,i) # backtrack
			


strarr = ['a','m','t','i','j','k']
len_arr = len(strarr)

permute(strarr,0,len_arr-1)

initit = lambda x: int(x)
stringit = lambda x : str(x)