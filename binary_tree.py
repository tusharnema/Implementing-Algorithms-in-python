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

root=Node(1)

root.left=Node(2)
root.right=Node(3)
root.left.left=Node(7)
root.left.right=Node(4)
root.right.left=Node(6)
root.right.right=Node(10)

printLevelOrder(root)
