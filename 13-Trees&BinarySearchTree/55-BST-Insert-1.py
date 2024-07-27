class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)                      # create a new nodde
        if self.root is None:                       # situation for empty tree.
            self.root = new_node                    #       root equals new node
            return True                             #       return true to stop code
        temp = self.root                            # use temp
        while (True):                               #
            if new_node.value == temp.value:        # situation if node is already in the tree. 
                return False                        #       you can't have duplicates, return false
            if new_node.value < temp.value:         # if node is less than temp value, go left
                if temp.left is None:               #       if spot is open...
                    temp.left = new_node            #               insert node
                    return True                     #               return true
                temp = temp.left                    #       if spot is closed, move temp to left
            else:                                   # ELSE-if node is more than temp value, go right
                if temp.right is None:              #       if spot is open..
                    temp.right = new_node           #               insert node  
                    return True                     #               return true
                temp = temp.right                   #       if spot is closed, move temp to right


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""