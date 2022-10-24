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


# break lists in half over and over and then merge (using recursion)
def merge_sort(my_list):
    # 1)base case: when len(the_list) is 1
    if len(my_list) == 1:         
        return my_list

    # 2)break lists in half.
    mid_index = int(len(my_list)/2) # get the middle index. if its an odd #, you cast to int so everything right to decimal place is dropped 
    left = my_list[:mid_index]      # (LEFT) starting point, empty so it is the first item. (RIGHT) we go up to BUT NOT including mix_index
    right = my_list[mid_index:]     # (LEFT) starting point: mid_index. (RIGHT) empty so it is the last item
    
    # 3)uses merge() to put lists together - MERGE REQUIRES TWO SORTED LISTS:
    return merge(merge_sort(left), merge_sort(right))   # call merge on left and right. call merge sort recursively to make sure the lists are sorted!!!




print(merge_sort([3,1,4,2]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4]
 """