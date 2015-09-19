intit = lambda x: int(x)
import math
def hasPerfectSquare(n):
	j = math.sqrt(n)
	return True if not j % 1 else False

def square_integer(numbers):
	numbers = numbers.split(" ")
	A,B = map(intit,numbers)
	count = 0 
	if B >= A:
		for x in range(A,B+1):
			if hasPerfectSquare(x):
				count += 1

	return count

# print square_integer("4 9")

t = input()
while t > 0:
	numbers = raw_input()
	print square_integer(numbers)
	t -= 1
