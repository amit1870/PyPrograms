class Queue(object):
	def __init__(self,limit=5):
		self.limit = limit
		self.front = None 
		self.rear = None
		self.size = 0
		self.que = []

	def isEmpty(self):
		return self.size <= 0

	def isFull(self):
		return self.size >= self.limit


	def enQueue(self,item):
		if self.isFull():
			print "Queue overflow"
			print "Resizing queue for reuse"
			self.resize()
			return
		self.que.append(item)
		
		if self.front is None:
			self.front = self.rear = 0
		else:
			self.rear = self.size

		self.size += 1

		print "After enqueue " , self.que

	def deQueue(self):
		if self.isEmpty():
			print "Queue underflow"
			return 0
		self.que.pop(0)
		self.size -= 1

		if self.size == 0:
			self.front = self.rear = None
		else:
			self.rear = self.size - 1
		print "After deque " , self.que

	def queFront(self):
		if self.isEmpty():
			print "Queue is empty"
			raise IndexError
		return self.que[self.front]

	def queRear(self):
		if self.isEmpty():
			print "Queue is empty"
			raise IndexError
		return self.que[self.rear]

	def resize(self):
		newQue = self.que
		self.limit *= 2
		self.que = newQue


que = Queue(5)
list = [9,34,28,38,89]
for item in list:
	que.enQueue(item)

que.deQueue()

que.enQueue(92)
que.enQueue(94)
print "Front " , que.queFront()
que.enQueue(29)
for item in xrange(1,10):
	que.enQueue(item)