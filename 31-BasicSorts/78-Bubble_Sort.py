# Bubble sort is the simplest sorting algorithm and a comparison-based algorithm.
# It runs through the list repeatedly from left to right, compares adjacent elements, 
# and swaps them if they are out of order. 
# The highest values are moved up the list.

def bubble_sort(my_list):                       # NOTE: range(start, stop, step)      
    for i in range(len(my_list) - 1, 0, -1):    # example: length of list = 6 (5 indexes)... start at 5, end at 0, decrement by 1. i never reaches the fir
        for j in range(i):                      #      i stores the length of list. j and j+1 store elements beside eachother. (PS: since we do j + 1, the previous for loop does until minus 1)!!!
            if my_list[j] > my_list[j+1]:       #           compare the 2 numbers next to each other going from left to right up until i
                temp = my_list[j]               #               switch these numbers               
                my_list[j] = my_list[j+1]       #
                my_list[j+1] = temp             #
    return my_list                              #


def print_test(my_list):                       
    for i in range(len(my_list) - 1, 0, -1):    
        for j in range(i):                      
                print("i at", i, "is", my_list[i])
                print("-----------")
                print("j at", j, "is", my_list[j])
        print("======================================")




print(bubble_sort([4,2,6,5,1,3]))


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