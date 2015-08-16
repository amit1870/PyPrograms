class SmartStack(object):
	"""
	This program is also helpful in finding the minimum of a list in one pass
	without using any sorting technique or comparing 

	"""
	def __init__(self):
		self.mainSt = []
		self.minSt = []

	def stack_push(self,x):
		self.mainSt.append(x)

		if not self.minSt or x <= self.stack_min():
			self.minSt.append(x)

	def stack_min(self):
		return self.minSt[-1]

	def stack_pop(self):
		x = self.mainSt.pop()
		if x == self.stack_min():
			self.minSt.pop()
		return x


def main():
	items = [2,4,8,9,0,1]
	stack = SmartStack()
	for x in items:
		stack.stack_push(x)
	print stack.mainSt
	print stack.minSt
	print stack.stack_min()
	stack.stack_push(-2)
	print stack.mainSt
	print stack.minSt
	print stack.stack_min()
	
	print stack.stack_pop()
	print stack.stack_pop()
	print stack.stack_pop()
	stack.stack_push(-6)
	print stack.mainSt
	print stack.minSt
	print stack.stack_min()
	


if __name__ == "__main__":
	main()

