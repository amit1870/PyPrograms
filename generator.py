def yrange(n):
	print "strating..."
	i = 0 
	while i < n:
		yield i*2 # each time the yield statement is executed
		i += 1  # the function generates a new value
		print "loop ", i


y = yrange(5)
print y
# print y.next()
for x in y :
	print x

def generator(n):
	return (2 * i for i in range(n))


x = generator(9)
print x.next()
print x.next()
print x.next()
