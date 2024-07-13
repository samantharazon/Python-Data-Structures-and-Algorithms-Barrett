class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size   # creates a list of seven spots with nothing in it
    

    # determine where to place the key value pair in the hash table
    # pass the key to determine the the address where we will store that key
    def __hash(self, key):
        my_hash = 0 # initialize varriable
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # 23 can be replaced with any prime number 
                                                                        # ord is short for ordinal which gets the ASCII number for each letter 
                                                                        # use % with the length which is 7 (default) to get the remainder...
                                                                        # If you divide any # by 7, remainder is going to be anywhere from zero to six...
                                                                        # and zero to six is the address space
        return my_hash  # return the # which is 0 to 6, which is 
                        # the address we use to place the key value pair in the hash table

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

        
my_hash_table = HashTable()

my_hash_table.print_table()

