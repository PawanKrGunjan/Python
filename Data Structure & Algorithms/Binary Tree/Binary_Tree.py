class BinarySearchTree :
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

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

def IsFoldable(root):
    if root is None:
        return True
    
    return isFoldableUntil(root.left, root.right)
    
def isFoldableUntil(l, r):
    if l == None and r == None:
        return True
    
    if l == None or r == None :
        return False

    a = isFoldableUntil(l.left, r.right)
    b = isFoldableUntil(l.right, r.left)
    return a and b

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 5]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(IsFoldable(tree))
    if IsFoldable(tree) is True:
        print("Yes")
    else :
        print("No")