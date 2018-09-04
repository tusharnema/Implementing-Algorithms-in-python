class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.count=1
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)
 
def insert(root,data):
    #print(root,data)
    if root is None:
        root=Node(data)
    
    elif root.data>data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root
def search(root,key):
    if root==None or root.data==key:
        return root
    else:
        if root.data>key:
            return search(root.left,key)
        else:
            return search(root.right,key)
 
 
 
def getMin(root):
    prev=None
    while root:
        prev=root
        root=root.left
    return prev
 
def getMax(root):
    prev=None
    while root:
        prev=root
        root=root.right
    return prev
 
def height(root):
    
    if root:
        return 1+max(height(root.left),height(root.right))
        
    return 0
 
def delete(root,data):
    if root is None:
        return None
    if root.data<data:
        root.right=delete(root.right,data)
    elif root.data>data:
        root.left=delete(root.left,data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        m=min(root.right)
        root.data=m.data
        root.right=delete(root.right,m.data)
    return root
 
 
def lcm(root,key1,key2):
    if key1>key2:
        key1,key2=key2,key1
        
    if root is None:
        return None
    if root.data>=key1 and root.data<=key2:
        return root
    else:
        if root.data>key1 and root.data>key2:
            return lcm(root.left,key1,key2)
        else:
            return lcm(root.right,key1,key2)

def sortedArrayToBST(arr):
    if not arr:
        return None
    mid=len(arr)//2
    root=Node(arr[mid])

    root.left=sortedArrayToBST(arr[:mid])
    root.right=sortedArrayToBST(arr[mid+1:])
    return root
 
def lca(root, x, y):
    if root is None:
        return None
    if (root.data < x and root.data < y):
        return lca(root.right, x, y)
    if (root.data > x and root.data > y):
        return lca(root.left, x, y)
    return root


root=None

root=insert(root,6)
root=insert(root,7)
root=insert(root,-2)
root=insert(root,4)
root=insert(root,1)
root=insert(root,9)
root=insert(root,11)
root=insert(root,5)

inorder(root)
print()
print(lca(root,1,5).data)