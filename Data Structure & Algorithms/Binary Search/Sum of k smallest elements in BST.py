"""class BinarySearchTree :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data :
            # add data in left subtree
            if self.left :
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

        
    def in_order_traversal(self):
        elements = []

        #Visit right tree
        if self.left:
            elements += self.left.in_order_traversal()

        #Visit Base node
        elements.append(self.data)

        #Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
"""

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None

# Function to Build Tree   
def buildTree(ip):
   
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
def in_order_traversal(root):
    elements = []

    #Visit right tree
    if root.left:
        elements += in_order_traversal(root.left)

    #Visit Base node
    elements.append(root.key)

    #Visit right tree
    if root.right:
        elements += in_order_traversal(root.right)

    return elements
def summ(root, k):
    # code here
    l = []
    l += in_order_traversal(root)
    #l = sorted(l)
    return sum(l[:k])

if __name__=="__main__":
    s= [10,14, 17, 7, 6, 5, 4]
    n=3
    root=buildTree(s)
    print(in_order_traversal(root))
    print(summ(root,n))
# } Driver Code Ends
