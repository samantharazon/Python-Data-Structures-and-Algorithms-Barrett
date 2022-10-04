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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:    # check for index out of range
            return False
        if index == 0:                          # add to beginning. if index = 0, call prepend method
            return self.prepend(value)
        if index == self.length:                # add to end. if index = last node, call append method
            return self.append(value)
        new_node = Node(value)                  # create node we're going to add
        temp = self.get(index - 1)              # set temp to node before the one we are inserting
        new_node.next = temp.next               # set new node to the one temp is pointing at
        temp.next = new_node                    # set temp's node to point to the new node
        self.length += 1   
        return True  
  



my_linked_list = LinkedList(1)
my_linked_list.append(3)
print('LL before insert():')
my_linked_list.print_list()


my_linked_list.insert(1,2)
print('\nLL after insert(2) in middle:')
my_linked_list.print_list()


my_linked_list.insert(0,0)
print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()


my_linked_list.insert(4,4)
print('\nLL after insert(4) at end:')
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""