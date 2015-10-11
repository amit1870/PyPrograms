def sortString(string):
	result = ""
	alpha = [0]*26

	len_str = len(string)

	for i in range(len_str):
		ch = ord(string[i])-ord('a')
		alpha[ch] += 1

	# Insert char a to z in resultant string that 
	# many number of times as they appear in input
	# string 

	for i in range(26):
		for j in range(alpha[i]):
			result += chr(i+97)
	return result

print sortString("amitpatel")

