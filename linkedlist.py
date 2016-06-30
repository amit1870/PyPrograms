class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class SingleLinkedList(object):
	def __init__(self):
		self.length = 0
		self.head = None

	def addNode(self,node):
		if self.length == 0:
			self.addBeg(node)
		else:
			self.addLast(node)

	def addBeg(self,node):
		newnode = node
		self.head = newnode
		self.length += 1

	def addLast(self,node):
		newnode = node
		current = self.head
		previous = self.head
		while current:
			previous = current
			current = current.next

		previous.next = newnode
		self.length += 1

	def printList(self):
		current = self.head
		items = []
		while current:
			items.append(current.data)
			current = current.next
		return items

	def addAtPos(self,node,p):
		newnode = node
		count = 0
		current = self.head
		previous = self.head
		while current and count < p-1:
			count += 1
			previous = current
			current = current.next

		if count != p - 1 :
			print "Fewer nodes in list"
			option = raw_input("Want to add in last(yes/no)? ")
			if option == "no":
				return
			else:
				self.addLast(node)
		previous.next = newnode
		newnode.next = current
		self.length += 1

	def delNode(self,p):
		if self.head is None:
			print "Linked List Underflow"
			return
		if p == 1 : 
			self.delBeg()

		else:
			previous = self.head
			current = self.head
			count = 0
			while current and count < p - 1:
				count += 1
				previous = current
				current = current.next

			previous.next = current.next
			current = None

			
	def delBeg(self):
		temp = self.head
		self.head = self.head.next
		temp = None

	def delLast(self):

		if self.head is None:
			print "Linked List Underflow"
			return

		previous = self.head
		if previous.next is None:
			self.delBeg()
			return

		current = self.head.next.next
		while current:
			previous = previous.next
			current = current.next

		lastNode = previous.next
		previous.next = current
		lastNode = None

	def delLinkedList(self):
		''' iterative version '''
		if self.head is None:
			print "Linked List Underflow"
			return
		else:
			current = self.head
			auxilary = self.head

			while current:
				auxilary = current.next
				current = None
				current = auxilary
			self.head = None

	def delLinkedListRecur(self):
		if self.head is None:
			return self.head
		else:
			auxilary = self.head.next
			self.head = None
			self.head = auxilary
			return self.delLinkedListRecur()

	def reverse(self):
		previous = None
		current = self.head
		next = None

		while current:
			next = current.next
			current.next = previous
			previous = current
			current = next
			
		self.head = previous

	def swap_nodes(self,x,y):
		if x == y :
			print "Both nodes are same."
			return
		prevX = None
		currentX = self.head
		while currentX != None and currentX.data != x:
			prevX = currentX
			currentX = currentX.next

		prevY = None
		currentY = self.head
		while currentY != None and currentY.data != y:
			prevY = currentY
			currentY = currentY.next

		if currentY == None or currentX == None:
			print "One of them is not present."
			return

		# if x is not head of list
		if prevX != None:
			prevX.next = currentY
		else:
			self.head = currentY

		# if y is not head of list
		if prevY != None:
			prevY.next = currentX
		else:
			self.head = currentX

		# swap two pointers
		temp = currentX.next
		currentX.next = currentY.next
		currentY.next = temp
		
	def detectLoop(self):
		slow = self.head
		fast = self.head

		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				print "Loop Found"
				self.removeLoop(slow)
				return True
				
	def removeLoop(self,loop_node):
		current = self.head

		while True:
			# Now start a pointer from loop_node and check if it ever reaches temp
			temp = loop_node
			while temp.next != loop_node and temp.next != current :
				temp = temp.next

			# If temp reached current then there is a loop, so break the loop
			if temp.next == current :
				break

			current = current.next

		# After the end of loop temp is the last node of the loop. So make next of temp as None
		temp.next = None
		
class CircularLinkedList(object):
	# constructor to create a empty circular linked list
	def __init__(self):
		self.head = None
		self.length = 0

	# fuction to insert a node at the begininng of a circular linked list
	def addBeg(self,node):
		newnode = node
		current = self.head

		newnode.next = self.head
		# if linked list is not None then set the next of last node
		if self.head is not None:
			while current.next != self.head :
				current = current.next
			current.next = newnode
		else:
			newnode.next = newnode

		self.head = newnode

	def printList(self):
		current = self.head
		nodes = []
		if self.head is not None:
			while True:
				nodes.append(current.data)
				current = current.next

				if current == self.head :
					break
		return nodes
		
	def split(self):
		if self.head is None:
			return
		tortoise = self.head
		hare = self.head
		
		while hare.next != self.head and hare.next.next != self.head:
			tortoise = tortoise.next
			hare = hare.next.next

		if hare.next.next is self.head:
			hare = hare.next

		t_head = self.head
		h_hear = tortoise.next
		hare.next = tortoise.next
		tortoise.next = self.head

		return t_head, h_hear
	
	def sorted_insertion(self,node):
		newnode = node
		current = self.head
		previous = self.head

		while current.data < newnode.data and current.next != self.head :
			previous = current
			current = current.next

		
		if current.next == self.head:
			current.next = newnode
			newnode.next = self.head

		elif previous == self.head :
			self.addBeg(newnode)
			
		else:
			previous.next = newnode
			newnode.next = current

singly = SingleLinkedList()
circular = CircularLinkedList()

nodes = []
for data in range(0,10,2):
	nodes.append(Node(data))

for node in nodes:
	# singly.addNode(node)
	circular.addBeg(node)

print circular.printList()
tortoise, hare = circular.split()

current = hare

while True:
	print current.data,
	current = current.next
	if current == hare:
		break

# creating a loop for testing
# singly.head.next.next.next.next.next = singly.head.next
# singly.detectLoop()

doubly = SingleLinkedList()
nodes = []
for data in range(0,10,3):
	nodes.append(Node(data))

for node in nodes:
	doubly.addNode(node)

