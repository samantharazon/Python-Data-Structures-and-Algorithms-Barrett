class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
      
    # creates the address
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    # will use hash method on key to create the address, then creates the key value pair and inserts it in a list in the hashtable
    def set_item(self, key, value):
        index = self.__hash(key)                    # get address where to store key value pair
        if self.data_map[index] == None:            # check if an empty list has already been created at the address. (remember: all addresses are initialized to None) if address space is None ...
            self.data_map[index] = []               #       intialize an empty list at the address where key value pair will be inserted
        self.data_map[index].append([key, value])   # put the key value pair into that empty list
    
        


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""