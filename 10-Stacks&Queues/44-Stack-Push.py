class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Method to push to top of stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:            # if list is empty
            self.top = new_node         #       set top to point to new node
        else:                           # else
            new_node.next = self.top    #       set new node's next to point to same node top is pointing to
            self.top = new_node         #       move top up to point to firt node
        self.height += 1
 



my_stack = Stack(2)
print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)    # calling push method
print('\nStack after push(1):')
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before push(1):
    2

    Stack after push(1):
    1
    2   

"""
