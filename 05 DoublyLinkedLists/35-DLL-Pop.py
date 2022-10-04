class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Method to pop last node
    def pop(self):
        if self.length == 0:            # case when there is no nodes
            return None
        temp = self.tail                # point temp to tail
        if self.length == 1:            # case when there is 1 node
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev  # move tail to node before it (the one left to it)
            self.tail.next = None       # break what tail points to
            temp.prev = None            # break what temp's previous is
        self.length -= 1
        return temp
  

  

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()
print()

# (2) Items - Returns 2 Node
print("popped:", my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print("popped:", my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print("popped:", my_doubly_linked_list.pop())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""