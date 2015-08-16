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


def postfixEvaluation(postfixexpr):
	opStack = Stack()
	postfixexpr = postfixexpr.split()
	for token in postfixexpr:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			opStack.push(token)
		else:
			operand2 = int(opStack.pop())
			operand1 = int(opStack.pop())
			result = doMath(token,operand1,operand2)

			opStack.push(result)
	return opStack.pop()
	

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print postfixEvaluation("1 2 3 * + 5 - ")