# efficient way. O(n)

# find if they have items in common
def item_in_common(list1, list2):
    my_dict = {}                # create dictionary
    for i in list1:             # for loop to go through list
        my_dict[i] = True       #       take values of that and put in dictionary

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1,3,5]
list2 = [2,4,6]


print(item_in_common(list1, list2))

