from queue import Queue
class BinaryTree(object):
	def __init__(self,data):
		self.data = data 
		self.left = None
		self.right = None

	# set data
	def setData(self, data):
		self.data = data
	# get data   
	def getData(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right

	def insertLeft(self,newNode):
		temp = BinaryTree(newNode)
		if self.left == None:
			self.left = temp

		else:
			temp.left = self.left
			self.left = temp

	def insertRight(self,newNode):
		temp = BinaryTree(newNode)
		if self.right == None:
			self.right = temp

		else:
			temp.right = self.right
			self.right = temp


def preOrder(root,result):
	if not root:
		return

	result.append(root.data)
	preOrder(root.left, result)
	preOrder(root.right, result)
	return result

def inOrder(root, result):
	if not root:
		return
	inOrder(root.left, result)
	result.append(root.data)
	inOrder(root.right, result)
	return result

def postOrder(root, result):
	if not root:
		return

	postOrder(root.left, result)
	postOrder(root.right, result)
	result.append(root.data)

	return result

def levelOrder(root, result):
    if root is None:
    	return
    q = Queue()
    q.enQueue(root)

    while not q.isEmpty():
    	node = q.deQueue()
    	result.append(node.data)

    	if node.left :
    		q.enQueue(node.left)
    	if node.right:
    		q.enQueue(node.right)

    return result


root = BinaryTree(9)
root.insertRight(21)
root.getRight().insertLeft(19)
root.getRight().insertRight(22)
root.insertLeft(8)
root.getLeft().insertLeft(4)
print "preorder: " ,preOrder(root,result=[])
print "inorder: ",inOrder(root, result=[])
print "postorder: ",postOrder(root, result=[])
print "levelorder: ", levelOrder(root,result=[])