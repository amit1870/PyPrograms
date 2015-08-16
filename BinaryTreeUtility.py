from BinaryTree import *
from stack import *
from queue import *

bn = BinaryTree(60)
bn.insertRight(70)
bn.getRight().insertLeft(65)
bn.insertRight(75)
bn.insertLeft(50)
bn.insertLeft(40)
bn.getLeft().insertRight(45)

"""
             60
            /   \
           50    70
          /  \   / \
         40  45 65  75


"""

print preOrder(bn,result=[])

def binaryTreeMax(root):
	if root:
		root_val = root.data
		left = binaryTreeMax(root.left)
		right = binaryTreeMax(root.right)
		max = left if left > right else right
		if max > root_val :
			return max
		else:
			return root_val
		

def binaryTreeMin(root):
	if root:
		root_val = root.data
		left = binaryTreeMin(root.left)
		right = binaryTreeMin(root.right)
		min = root_val
		if left and right is not None:
			min = left if left < right else right

		if min < root_val:
			return min
		else:
			return root_val

def searchElement(root,key):
	if root:
		if key == root.data:
			return True
		else:
			left = searchElement(root.left,key)

			if left:
				return left
			right = searchElement(root.right, key)
			if right:
				return right
			else:
				return False

def sizeOfBinaryTree(root):
	if root:
		return sizeOfBinaryTree(root.left) + 1 + sizeOfBinaryTree(root.right)
	else:
		return 0

def levelOrderInReverse(root,result):
	if root:
		q = Queue()
		s = Stack()
		q.enQueue(root)
		while not q.isEmpty():
			node = q.deQueue()
			if node.right :
				q.enQueue(node.right)
			if node.left:
				q.enQueue(node.left)
			
			s.push(node.data)

		while not s.isEmpty():
			result.append(s.pop())

		return result

def deleteTree(root):
	if root is None:
		return 
	deleteTree(root.left)
	deleteTree(root.right)
	root = None

def heightOfTree(root):
	if root:
		left_height = heightOfTree(root.left)
		right_height = heightOfTree(root.right)
		
		return max(right_height,left_height) + 1

	else:
		return 0

def deepestNode(root):
	if root:
		q = Queue()
		q.enQueue(root)
		while not q.isEmpty():
			node = q.deQueue()
			if node.left:
				q.enQueue(node.left)
			if node.right:
				q.enQueue(node.right)

		return node.data

def findElement(root,key):
	if root:
		if key == root.data:
			return root
		else:
			left = searchElement(root.left,key)

			if left:
				return left
			right = searchElement(root.right, key)
			if right:
				return right
			else:
				return False

def deleteNode(root,key):
	if root:
		if findElement(root,key):
			deep_node = deepestNode(root)
			temp = findElement(root,key)
			print temp
			temp = deep_node
			deep_node = None	


# print "max of binary tree ",binaryTreeMax(bn)

# print "min of binary tree ",binaryTreeMin(bn)

# print "Found ",searchElement(bn,73)

# print "size: %d" %sizeOfBinaryTree(bn)

# print "level order in reverse: " , levelOrderInReverse(bn,result=[])

# print deleteTree(bn)

# print "Height of tree: "  , heightOfTree(bn)

# print deepestNode(bn)

print findElement(bn,65)
print deleteNode(bn,65)