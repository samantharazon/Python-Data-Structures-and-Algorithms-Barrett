class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # Method to add to end of line
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:          # case where queue is empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node   # node where last currently is has next point new node
            self.last = new_node        # last moves to new node
        self.length += 1
        



my_queue = Queue(1)
print('Queue before enqueue(2):')
my_queue.print_queue()


my_queue.enqueue(2)
print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""