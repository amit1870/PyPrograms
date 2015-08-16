from stack import *
from queue import *

st = Stack()
que1 = Queue()
que2 = Queue()

for x in xrange(1,10):
	if que1.isEmpty():
		que2.enQueue(x)
	else:
		que1.enQueue(x)

print que2.que

len_que2 = len(que2.que)
i = 0
while i < len_que2 - 1:
	que1.enQueue(que2.deQueue())
	i += 1

print que1.que
print que2.deQueue()
