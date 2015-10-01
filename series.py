def checkSeries(seq):
	if len(seq) > 1:
		a = seq[0]

		d = seq[1] - seq[0]

		for i in range(1,len(seq)):
			new_d = seq[i] - seq[i-1]
			if new_d != d:
				return False
		return True


print checkSeries([6,10,14,18,19])
