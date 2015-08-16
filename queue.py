class Queue(object):
	def __init__(self, limit=10):
		self.limit = limit
		self.que = []
		self.rear = None
		self.front = None

	def enQueue(self, item):
		self.que.append(item)

	def deQueue(self):
		return self.que.pop(0)

	def printQueue(self):
		print  self.que

	def resize(self):
		newQue = self.que
		self.que *= 2
		self.que = newQue

	def isEmpty(self):
		return self.que == []

	def isFull(self):
		return self.size == self.limit