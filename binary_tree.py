from collections import deque
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def printLevelOrder(root):
	dq=deque()
	temp=root

	while temp is not None:
		print(temp.data)
		dq.append(temp.left)
		dq.append(temp.right)
		temp=dq.popleft()

def height(root):
	if(root):
		return 1+max(height(root.left),height(root.right))
	return 0

def identical(root1,root2):
	if(root1 is None and root2 is None):
		return True
	if(root is not None and root2 is not None):
		return ((root1.data==root2.data) and identical(root1.left,root2.left) and identical(root1.right,root2.right))
	return False

def getleafcount(root):
	if(root is None):
		return 0
	if(root.left is None and root.right is None):
		return 1
	else:
		return (getleafcount(root.left)+ getleafcount(root.right))

root=Node(1)

root.left=Node(2)
root.right=Node(3)
root.left.left=Node(7)
root.left.right=Node(4)


