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
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    # Method to dequeue from beginning 
    def dequeue(self):
        if self.length == 0:                # case where there is no items in queue
            return None
        temp = self.first                   # temp points to first node
        if self.length == 1:                # case where there is 1 node
            self.first = None
            self.last = None
        else:
            self.first = self.first.next    # move first to point to node to the right of it
            temp.next = None                # remove temp
        self.length -= 1
        return temp

 

 
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()
print("-------------")

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
print()
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
print()
# (0) Items - Returns None
print(my_queue.dequeue())
print()



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""