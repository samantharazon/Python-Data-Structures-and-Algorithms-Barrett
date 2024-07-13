# The selection sort algorithm sorts an array by repeatedly finding the minimum element 
# from the unsorted part and putting it at the beginning. 
# The algorithm maintains two subarrays in a given array. The subarray which already sorted.

def selection_sort(my_list):                    # NOTE: range(start, stop, step)      
    for i in range(len(my_list)-1):             # example: length of list = 6 (5 indexes): since i just goes through indexes 1 to 4, we do minus one. later we compare i + 1. i never needs to reach the end of the list     
        min_index = i                           #   initialize min index to current position of i      
        for j in range(i+1, len(my_list)):      #   start at the value after i. compare the 2 numbers next to each other going from left to right up until the length of the list    
            if my_list[j] < my_list[min_index]: #       if value at j is less than value at min_index....          
                min_index = j                   #          store index of j to min_index
        if i != min_index:                      #       if i equals min_index, that value is already sorted. only if they are not equal, continue
            temp = my_list[i]                   #               swap value at i with value at min_index. This will put the smallest element at the beginning
            my_list[i] = my_list[min_index]     #               
            my_list[min_index] = temp           #               
    return my_list                              # 


def print_test(my_list):                    
    for i in range(len(my_list)-1):             
        for j in range(i+1, len(my_list)):     
            print("i at", i, "is", my_list[i])
            print("-----------")
            print("j at", j, "is", my_list[j])
        print("======================================")
            


print(selection_sort([4,2,6,5,1,3]))

print("\n======================================")
my_list = [4,2,6,5,1,3]
print(my_list)
print()
print_test(my_list)
 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

