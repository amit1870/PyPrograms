def fibo(n):
	if n <= 1:
		return n 

	else:
		return fibo(n-1) + fibo(n-2)


# start = input("Enter starting range :")
# end = input("Enter end point ")

# print map(fibo, range(start, end))