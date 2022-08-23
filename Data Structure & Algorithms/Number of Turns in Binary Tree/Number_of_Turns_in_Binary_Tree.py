print('''
Number of Turns in Binary Tree : Given a binary tree and data value of two of its nodes. 
Find the number of turns needed to reach from one node to another in the given binary tree. ''')
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None

# Function to Build Tree  
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input string after spliting by space
    ip=list(map(str,s.split()))
    
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

def findLCA(root, n1, n2):
	# Base case
	if root is None:
		return None
    
	#If either n1 or n2 matches with root's key, 
    #report the presence by returning root (Note that if a key is ancestor of other,
    #then the ancestor key becomes LCA
    
	if root.key == n1 or root.key == n2:
		return root

	# Look for keys in left and right subtrees
	left_lca = findLCA(root.left, n1, n2)
	right_lca = findLCA(root.right, n1, n2)

	# If both of the above calls return
	# Non-NULL, then one key is present
	# in once subtree and other is present
	# in other, So this node is the LCA
	if left_lca and right_lca:
		return root

	# Otherwise check if left subtree or right
	# subtree is LCA
	return (left_lca if left_lca is not None else right_lca)

# function count number of turn need to reach
# given node from it's LCA we have two way to
def countTurn(root, key, turn):
	global count
	if root is None:
		return False

	# if found the key value in tree
	if root.key == key:
		return True

	# Case 1:
	if turn is True:
		if countTurn(root.left, key, turn):
			return True
		if countTurn(root.right, key, not turn):
			count += 1
			return True

	# Case 2:
	else:
		if countTurn(root.right, key, turn):
			return True
		if countTurn(root.left, key, not turn):
			count += 1
			return True
	return False

# Function to find nodes common to given two nodes

# Function to find nodes common to given two nodes
def NumberOFTurns(root: Node, first: int, second: int) -> int:
    global count
    LCA = findLCA(root, first, second)
 
    # there is no path between these two node
    if LCA is None:
        return -1
 
    count = 0
 
    # case 1:
    if LCA.key != first and LCA.key != second:
 
        # count number of turns needs to reached
        # the second node from LCA
        if countTurn(LCA.right, second, False) or countTurn(
                LCA.left, second, True):
            pass
 
        # count number of turns needs to reached
        # the first node from LCA
        if countTurn(LCA.left, first, True) or countTurn(
                LCA.right, first, False):
            pass
        return count + 1
 
    # case 2:
    if LCA.key == first:
 
        # count number of turns needs to reached
        # the second node from LCA
        countTurn(LCA.right, second, False)
        countTurn(LCA.left, second, True)
        return count
    else:
 
        # count number of turns needs to reached
        # the first node from LCA1
        countTurn(LCA.right, first, False)
        countTurn(LCA.left, first, True)
        return count


if __name__=="__main__":    
    s ='1 2 3 4 5 6 7 8 N N N 9 10 N N'
    print(s)
    root=buildTree(s)
    n1,n2=list(map(int, input().strip().split())) 
    turn = NumberOFTurns(root,n1,n2)
    if turn!=0:
        print(turn)
    else:
        print(-1)
