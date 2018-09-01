class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.count=1
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,"-->",root.count)
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
 
 
    
q=int(input())
root=None
for i in range(q):
    input_str=input()
    if input_str=='CountHigh':
        print(getMax(root).count if root is not None else -1)
 
    elif input_str=='CountLow':
        print(getMin(root).count if root is not None else -1)
 
    elif input_str=='Diff':
        ma=getMax(root)
        mi=getMin(root)
        if ma is None and mi is None:
            print(-1)


 
