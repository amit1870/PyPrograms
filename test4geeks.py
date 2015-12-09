def func():
	return 1,2,3

''' this will unpack the argument as tuple.'''
a = func() 
''' this will raise a ValueError to many value to unpack'''
# a,b = func()
# (a,b) = func()

# try except block
(x,y) = (5,0)
try:
	z = x/y
except ZeroDivisionError as e:
	z = e
	# raise
else:
	print z
finally:
	print "it"
