def lexoString(word):
	word = list(word)
	# find non-increasing suffix 
	i = len(word) - 1
	while  i > 0 and word[i-1] >= word[i]:
		i -= 1 
	if i <= 0:
		return "no answer"

	print i
	# find successor to pivot 
	j = len(word) - 1
	while word[j] <= word[i-1] :
		j -= 1
	print j
	# exchanging pivot with next greatest element
	word[i-1], word[j] = word[j], word[i-1]
	
	# reverse suffix 
	print word,i
	temp = word[len(word)-i : i-1 : -1]
	print temp
	word = word + temp
	return "".join(word)
	

# T = input()
# while T > 0:
# 	word = raw_input()
# 	print lexoString(word)
# 	T -= 1
print lexoString("haibcdegf")