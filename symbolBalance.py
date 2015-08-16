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

		# print self.stk

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

	def isMatchingPair(self,a,b):
		if a == '(' and b == ')' or a == '{' and b == '}' or a == '[' and b == ']':
			return 1
		return 0

	def areParenthesisBalanced(self,string):
		i = 0

		while string[i] :
			if string[i] == '(' or string[i] == '{' or string[i] == '[':
				self.push(string[i])
				
			if string[i] == ')' or string[i] == '}' or string[i] == ']':
				if self.isEmpty():
					return 0
				if not self.isMatchingPair(self.pop(),string[i]):
					return 0

			i += 1
			if len(string) == i:
				break

		if self.isEmpty():
			return 1
		return 0

string = "(5+4)-(32*43(89))*{[{23}]}"
stack = Stack(50)
print stack.areParenthesisBalanced(string)


