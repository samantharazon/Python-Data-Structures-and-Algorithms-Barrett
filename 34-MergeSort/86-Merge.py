# The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm. 
# In this algorithm, the array is initially divided into two equal halves 
# and then they are combined in a sorted manner.


# sort two lists
def merge(list1, list2):
    combined = []                               # 
    i = 0                                       # i points to first list
    j = 0                                       # j points to second list
    # sort while both lists have items
    while i < len(list1) and j < len(list2):    # as long as both lists still have items
        if list1[i] < list2[j]:                 #   if i is less than j
            combined.append(list1[i])           #       append to combined list, the item at index of i
            i += 1                              #       move i over one
        else:                                   #   else, 
            combined.append(list2[j])           #       append to combined list, the item at index of j
            j += 1                              #       move j over one
    
    # sort while one list is empty while the other has items
    while i < len(list1):                       # while i has items
        combined.append(list1[i])               #       append to combined list, the item at index of i
        i += 1                                  #       move i over one

    while j < len(list2):                       # while j has items
        combined.append(list2[j])               #       append to combined list, the item at index of j
        j += 1                                  #       move j over one

    return combined




# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """