class BSTNode(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


def insertNode(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data :
			if root.left is None:
				root.left = node
			else:
				insertNode(root.left,node)

		else:
			if root.right is None:
				root.right = node
			else:
				insertNode(root.right, node)

def inOrder(root,result):
	if not root:
		return 
	inOrder(root.left, result)
	result.append(root.data)
	inOrder(root.right, result)
	return result

def searchElement(root,data):
	if not root:
		return None
	else:
		if data < root.data:
			return searchElement(root.left, data)
		elif data > root.data:
			return searchElement(root.right, data)
		return root.data

def findMin(root):
	if not root:
		return None
	else:
		if root.left is None:
			return root.data
		else:
			return findMin(root.left)


def findMax(root):
	if not root:
		return None
	else:
		if root.right is None:
			return root.data
		else:
			return findMax(root.right)

def deleteNode(root,data):
	if not root:
		return
	else:
		if data < root.data:
			root.left = deleteNode(root.left, data)
		elif data > root.data:
			root.right = deleteNode(root.right, data)
		else:
			if root.left and root.right: # having both child 
				temp = findMax(root.left)
				root.data = temp
				root.left = deleteNode(root.left, root.data)
			else:
				# one child 
				temp = root
				if root.left is None:
					root = root.right
				else:
					root = root.left
				temp = None
	return root

def isBST(root):
	if not root:
		return True 
	else:
		if root.left and root.left.data > root.data:
			return False
		if root.right and root.right.data < root.data:
			return False
		if not isBST(root.left) or not isBST(root.right):
			return False
		
		return True






root = BSTNode(89)

for x in [17,8,15,90,76,786]:
	insertNode(root,BSTNode(x))


print inOrder(root,result=[])

print searchElement(root,17)

print findMin(root)

print findMax(root)

deleteNode(root,76)
deleteNode(root,89)

print inOrder(root,result=[])
print isBST(root)