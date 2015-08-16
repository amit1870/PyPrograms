from stack import *
from queue import *

q = Queue()
s1 = Stack()
s2 = Stack()

for x in xrange(10,100):
	s1.push(x)

if not s2.isEmpty() :
	s2.pop()

if s2.isEmpty():
	while not s1.isEmpty():
		s2.push(s1.pop())

print s2.pop()
print s2.pop()