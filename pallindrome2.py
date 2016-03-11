def shortPallin(s):
	len_s = len(s)
	j = len_s - 1
	count = 0 
	for i in range(0,len_s):
		if i <= j:
			if s[i] != s[j] :
				count += 1
			else:
				j -= 1
		else:
			break
	return count

s = "abcxyzmno"
print shortPallin(s)

