class PriorityQueue(object):
	
	def __init__(self,arry):
		self.arry = arry
		self.length = len(self.arry) - 1
		self.build_max_heap()

	def build_max_heap(self):
		for i in range(self.length/2,-1,-1):
			self.max_heapify(i)

	def swap(self,i,j):
		tmp = self.arry[i]
		self.arry[i] = self.arry[j]
		self.arry[j] = tmp

	def max_heapify(self,i):
		left = 2 *i + 1
		right = 2*i + 2
		if left <= self.length and self.arry[left] > self.arry[i]:
			largest = left
		else:
			largest = i

		if right <= self.length and self.arry[right] > self.arry[largest]:
			largest = right
		if largest != i:
			self.swap(i,largest)
			self.max_heapify(largest)
		else:
			return

	def heap_maximum(self):
		if self.arry:
			return self.arry[0]

	def heap_extract_max(self):
		if self.length < 1:
			print "Heap underflow"
			return
		else:
			max = self.arry[0]
			self.arry[0] = self.arry[self.length]
			self.length = self.length - 1
			self.arry.pop()
			self.max_heapify(0)
			return max

	def heap_increase_key(self,i,key):
		if key < self.arry[i]:
			print "new key is smaller than current key"
			return
		self.arry[i] = key
		while i > 0 and self.arry[(i/2)-1] < self.arry[i]:
			self.swap(i,(i/2)-1)
			i = (i/2)-1

	def max_heap_insert(self,key):
		self.arry.append(None)
		self.length = self.length + 1
		self.heap_increase_key(self.length,key)

pq = PriorityQueue([32,3,45,6,7,7,32,45,65,43,12,8])
print pq.arry

print pq.heap_extract_max()
print pq.arry

pq.heap_increase_key(2,90)
print pq.arry

pq.max_heap_insert(23)
print pq.arry