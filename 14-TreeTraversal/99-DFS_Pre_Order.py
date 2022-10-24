# DFS is also a traversal approach in which the traverse begins at the root node 
# and proceeds through the nodes as far as possible 
# until we reach the node with no unvisited nearby nodes.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    
    # Inorder => Left, Root, Right.
    # Preorder => Root, Left, Right.
    # Post order => Left, Right, Root.
    def dfs_pre_order(self):
        results = []
        # ------------------------------------------
        def traverse(current_node):
            results.append(current_node.value)  # append to results value of current node
            if current_node.left is not None:   # if there is a node to the left of it
                traverse(current_node.left)     #   recursivey run traverse
            if current_node.right is not None:  # if there is a node to the right of it
                traverse(current_node.right)    #   recursivey run traverse
        # ------------------------------------------
        traverse(self.root)  # call function traverse
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.dfs_pre_order())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 18, 27, 76, 52, 82]

 """

                

