intit = lambda x: int(x)

def sqaure_root(n):
	temp = n
	flag = False
	dict = {}
	while temp != 1:

		if isPrime(temp) and not flag:
			return False

		if isEven(temp):
			temp /= 2
			update_dict(dict,2)
			flag = True

		if temp % 3 == 0:
			temp /= 3
			update_dict(dict,3)
			flag = True

		if temp % 5 == 0:
			temp /= 5
			update_dict(dict,5)
			flag = True

		for i in range(11,n/2+1):
			if isPrime(i) and temp % i == 0:
				temp /= i
				update_dict(dict,i)

	return dict












def update_dict(dict,n):
	if dict.has_key(n):
		dict[n] += 1
	else:
		dict[n] = 1


def isPrime(n):
	for i in range(2,n/2+1):
		if n % i == 0:
			return False
	return True

def isEven(n):
	return n % 2 == 0

print sqaure_root(1024)

# t = input()
# while t > 0:
# 	n = input()
# 	print sqaure_root(1024)
# 	t -= 1
