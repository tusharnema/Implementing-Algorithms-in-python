class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
 
##def insert(root,data):
##    #print(root,data)
##    if root is None:
##        root=Node(data)
##    elif root.data>data:
##        root.left=insert(root.left,data)
##    else:
##        root.right=insert(root.right,data)
##
##    return root
 
 
 
def insert(root,key):
    curr = root;
    parent = None;
    if (root  is None):
        return Node(key)
 
 
    while curr is not None:
        parent = curr;
        if (key < curr.data):
            curr = curr.left
        else:
            curr = curr.right;
    if (key < parent.data):
        parent.left =Node(key);
    else:
        parent.right = Node(key);
 
    return root;
 
    
def search(root,key):
    if root==None or root.data==key:
        return root
    else:
        if root.data>key:
            return search(root.left,key)
        else:
            return search(root.right,key)
 
 
def getMax(root):
    prev=None
    while root:
        prev=root
        root=root.right
    return prev.data if prev is not None else -1
 
def getMin(root):
    prev=None
    while root:
        prev=root
        root=root.left
    return prev.data if prev is not None else -1
 
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
        m=getMin(root.right)
        root.data=m
        root.right=delete(root.right,m)
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
 