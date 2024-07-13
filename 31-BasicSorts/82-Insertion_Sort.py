# Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time by comparisons.
# The first element in the array is considered as sorted, even if it is an unsorted array
# Each element in the array is checked with the previous elements, 
# resulting in a growing sorted output list. 
# With each iteration, the sorting algorithm removes one element at a time and finds 
# the appropriate location within the sorted array and inserts it there. The iteration continues until the whole list is sorted.

def insertion_sort(my_list):                    # NOTE: range(start, stop, step)      
    for i in range(1, len(my_list)):            # start at index 2. in other words, go from index 1 to end of list
        temp = my_list[i]                       #   hold value at index i
        j = i-1                                 #   set j to item at index before i
        while temp < my_list[j] and j > -1:     #   while temp is less than item before it AND if j is equal to -1, STOP!
            my_list[j+1] = my_list[j]           #       at the index of j + 1, value of j moves there
            my_list[j] = temp                   #       at the index of j, value of temp moves there
            j -= 1                              #       move index of j over 1 to the left (and run while loop again until it breaks)
    return my_list

print(insertion_sort([4,2,6,5,1,3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

