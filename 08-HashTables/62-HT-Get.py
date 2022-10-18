class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    # get the address of the key, loop through key value pairs until you get to the key, and return the value of the key
    def get_item(self, key):
        index = self.__hash(key)                        # get address where to store key value pair
        if self.data_map[index] is not None:            # check if a key value pair exists at that address. if items are there...
            for i in range(len(self.data_map[index])):  #       loop through all the key value pairs in the list at that index (addresss space)
                if self.data_map[index][i][0] == key:   #       self.data_map[index] refers to the list at address space. 
                                                        #       .. [i] is i from the for loop. We are looking at the item thats at the index of i. This gives us the key-value pair at the index in a list
                                                        #       .. [0] will look at the key (ex 'bolts')
                                                        #       .. = key says -> does that match the key, the one we passed to the method? (if no, continue running for loop)
                                                        #       .. SUMMARY: Look at it like "self.data_map[index][i]" gets the current key-value pair. [0] tells it we only want the key
                    return self.data_map[index][i][1]   #               return at that index at the i, the value of the key
        return None                                     # else, return none

        
             

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

my_hash_table.print_table()

print('\nGet value of bolts:')
print('Bolts:', my_hash_table.get_item('bolts'))

print('\nGet value of washers:')
print('Washers:', my_hash_table.get_item('washers'))

print('\nGet value of lumbers:')
print('Lumber:', my_hash_table.get_item('lumber'))



"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""