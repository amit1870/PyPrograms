def lexoString(word):
	word = list(word)
	# find non-increasing suffix 
	i = len(word) - 1
	while  i > 0 and word[i-1] >= word[i]:
		i -= 1 
	if i <= 0:
		return "no answer"

	# find successor to pivot
	j = len(word) - 1
	while word[j] <= word[i-1] :
		j -= 1

	# exchanging pivot with next greatest element
	word[i-1], word[j] = word[j], word[i-1]



	# after exchaning words split into two part and reverse the right 
	left = word[:i]
	right = word[i:]
	right.reverse()
	word = left+right
	
	return "".join(word)
	

T = input()
while T > 0:
	word = raw_input()
	print lexoString(word)
	T -= 1