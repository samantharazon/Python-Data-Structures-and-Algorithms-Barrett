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
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # take all the keys out of the hash table, put them into a list, and return that list
    def keys(self):
        all_keys = []                                           # create empty list where we put all the keys in
        for i in range(len(self.data_map)):                     # for loop moves through the entire hash table
            if self.data_map[i] is not None:                    #       check if that space has items. If a key value pair exists at that address. if items are there...
                for j in range(len(self.data_map[i])):          #                loop through the list with all the key value pairs at the current index (addresss space)
                    all_keys.append(self.data_map[i][j][0])     #                       to all keys list, append the key for each key value pair in the list at the current index       
        return all_keys                                         # return that list
        

        

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()

print("\nAll the keys in the hash table:")
print(my_hash_table.keys())



"""
    EXPECTED OUTPUT:
    ----------------
    ['bolts', 'washers', 'lumber']

"""