class Stack(object):
	def __init__(self,limit=5):
		self.stk = []
		self.limit = limit

	def isEmpty(self):
		return len(self.stk) <= 0

	def isFull(self):
		return len(self.stk) >= self.limit

	def push(self,item):
		if self.isFull() :
			print "Stack overflow"
		else:
			self.stk.append(item)

		print self.stk

	def pop(self):
		if self.isEmpty():
			print "Stack underflow"
			return 0
		else:
			return self.stk.pop()

	def peek(self):
		if self.isEmpty():
			print "Stack underflow"
			return 0
		else:
			return self.stk[-1]

	def size(self):
		return len(self.stk)

stack = Stack(20)
stack.push(20)
stack.push(30)
stack.push(303)
print stack.peek()
