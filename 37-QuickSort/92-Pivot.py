# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
# It picks an element as a pivot and partitions the given array around the picked pivot. 
# There are many different versions of quickSort that pick pivot in different ways. 

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# VARIABLES:
# - pivot_index is the first element in list used to compare values
# - i is used to traverse list one by one after pivot and compare to pivot value
# - swap_index is used to swap values less than pivot. it swaps less value with the first greater value. first swap moves by one, then it swaps with i. when i reaches end, swap then swaps with pivot

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index                    # swap is initially equal to the pivot which is first element in list

    for i in range(pivot_index+1, end_index+1): # i starts at pivot + 1 which is second element in list, for loop will go up to but not including the end_index + 1
        if my_list[i] < my_list[pivot_index]:   #   value at i is compared to pivot. if less than pivot,
            swap_index += 1                     #       move swap over one
            swap(my_list, swap_index, i)        #       swap items at i and swap
    swap(my_list, pivot_index, swap_index)      # swap items at pivot and swap
    return swap_index                           # return the INDEX of the swap




my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6) # set pivot to be first item in list (0) and pass in last index of list (6)

print('\nList after running pivot():')
print(my_list)

print('\nPivot Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Pivot Index:
    3

 """