# checking if a number is power of 2

def isPowerofTwo(num):
	if num > 0 and num & num-1 == 0 :
		return True

	return False

print isPowerofTwo(16)