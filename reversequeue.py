from stack import *
from queue import *

que = Queue()
stk = Stack()
for x in range(2,10):
	que.enQueue(x)

que.printQueue()
while que.que:
	stk.push(que.deQueue())

while stk.stk:
	que.enQueue(stk.pop())

print que.printQueue()
print que.deQueue()