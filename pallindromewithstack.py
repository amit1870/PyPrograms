class SimpleStack(object):
	def __init__(self):
		self.stack = []

	def stack_push(self,item):
		self.stack.append(item)

	def stack_pop(self):
		return self.stack.pop()

	def stack_top(self):
		return self.stack[-1]


def main():
	st = SimpleStack()

	string = "abcXcba"
	i = 0
	while string[i] != 'X':
		st.stack_push(string[i])
		i += 1


	i += 1
	while i < len(string) :
		if st.stack == [] or string[i] != st.stack_pop():
			print "Not Pallindrome"
			return None
		i += 1

	print "Pallindrome"
	
if __name__ == "__main__":
	main()