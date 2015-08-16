class Stack(object):
	def __init__(self):
		self.stk = []

	def push(self,item):
		self.stk.append(item)

	def pop(self):
		return self.stk.pop()

	def isEmpty(self):
		return (self.stk == [])
		
	def peek(self):
		return self.stk[-1]

	def __str__(self):
		return str(self.stk)
