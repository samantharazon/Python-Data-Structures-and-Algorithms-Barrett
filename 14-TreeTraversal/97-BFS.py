# BFS is a traversal approach in which we first walk through all nodes on the same level 
# before moving on to the next level.

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
    
   
    # YOU CAN ALSO WRITE BFS WITH A QUEUE INSTEAD OF LIST
    # (TECHNICALLY THIS IS A BETTER SOLUTION)
    #
    # def BFS(self):
    #     current_node = self.root
    #     queue = Queue()
    #     results = []
    #     queue.put(current_node)

    #     while not queue.empty():
    #         current_node = queue.get()
    #         results.append(current_node.value)
    #         if current_node.left is not None:
    #             queue.put(current_node.left)
    #         if current_node.right is not None:
    #             queue.put(current_node.right)
    #     return results
                
    # step 1: set root equal to current node and add it to queue
    # step 2: pop the first item from the queue, add it to results
    #         check if it that item has a left child, add it to queue
    #         check if it that item has a right child, add it to queue
    # step 3: continue step 2
    def BFS(self):
        current_node = self.root                    # root is current node

        queue = []                                  #
        results = []                                #

        queue.append(current_node)                  # append to queue the current node. this also stores remembers the left and right of the node

        while len(queue) > 0:                       # while the queue is not empty...
            current_node = queue.pop(0)             #   pop from queue the first item and set it to the current node
            results.append(current_node.value)      #   add the value of the current node to results
            if current_node.left is not None:       #   if there is a node to the left of current one
                queue.append(current_node.left)     #       add that left node to the queue
            if current_node.right is not None:      #   if there is a node to the right of current one
                queue.append(current_node.right)    #       add that right node to the queue
        return results                              #





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())



"""
    EXPECTED OUTPUT:
    ----------------
    [47, 21, 76, 18, 27, 52, 82]

 """





                



 