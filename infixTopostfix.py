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

def infixToPostfix(infixexpr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1

	opStack = Stack()

	postfixexpr = []

	tokenList = infixexpr.split()

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixexpr.append(token)

		elif token == '(':
			opStack.push(token)

		elif token == ')':
			topToken = opStack.pop()
			while topToken != '(':
				postfixexpr.append(topToken)
				topToken = opStack.pop()

		else:
			while (not opStack.isEmpty()) and \
				(prec[opStack.peek()]) >= prec[token]:
					postfixexpr.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixexpr.append(opStack.pop())

	return " ".join(postfixexpr)

print infixToPostfix("A * B + C * D")	
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

