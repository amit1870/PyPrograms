from stack import Stack

def infixInOnePass(infixexpr):
	operatorStack = Stack()
	operandStack = Stack()

	infixexpr = infixexpr.split()

	i = 0

	for token in infixexpr:
		next_token = infixexpr[i+1]
		if next_token in "0123456789":
			operandStack.push(next_token)

		else:
			


print infixInOnePass("20 + ( 63 * 9 ) + 30")
