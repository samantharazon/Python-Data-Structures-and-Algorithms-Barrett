class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Method to pop node from end
    def pop(self):
        if self.length == 0:    # scenario that length we started is none
            return None
        temp = self.head
        pre = self.head
        while(temp.next):       # while temp is pointing to a node (we move it over)
            pre = temp          #       move pre to equal temp
            temp = temp.next    #       move temp over
        self.tail = pre         # move tail equal to pre
        self.tail.next = None   # pop off last node
        self.length -= 1
        if self.length == 0:    # situation where we have 1 node only. after decremening length by 1... now length is = 0
            self.head = None
            self.tail = None
        return temp             # return node popped

 


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""