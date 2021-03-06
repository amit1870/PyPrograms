def consecutive(seq):
	prevCount = 1
	currentCount = 1

	first = seq[0]
	index = 0
	for i in range(1,len(seq)):
		if seq[i] == first + 1:
			currentCount += 1
			prevCount = currentCount if currentCount > prevCount else prevCount
		else:
			currentCount = 1
		first = seq[i]

	return prevCount, i + 1 - prevCount

print consecutive([2,3,4,10,11,12,13,14,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10])

def matching(string,pattern,count):
	len_s = len(string)
	i = 0
	match = 0
	while i < len_s-len(pattern)+1:
		seq = []
		for j in range(i,i+len(pattern)):
			seq.append(string[j])
			if len(seq) == len(pattern):
				if "".join(seq) == pattern:
					match +=1 
				else:
					break
			
		i += 1

	# print count,match
	if count == match:
		return True

	return False



print matching("amitpatelmamtapatellalbahadurpatel","patel",3)
