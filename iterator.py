class Reverse:
	""" Iterator for looping over a sequence backwards."""

	def __init__(self,data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

rev = Reverse('Span')
rev = iter(rev)
for ch in rev:
	print ch


""" Generators """
def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

for ch in reverse('golf'):
	print ch