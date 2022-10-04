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
    
    # Method to append to list
    def append(self, value):
        new_node = Node(value)              # create a new node
        if self.head is None:               # if it is empty...
            self.head = new_node            #   head is equal to new node
            self.tail = new_node            #   tail is equal to new node
        else:
            self.tail.next = new_node       
            new_node.prev = self.tail       
            self.tail = new_node
        self.length += 1
        return True
  



my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2
    
"""
