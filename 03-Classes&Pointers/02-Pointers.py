num1 = 11

num2 = num1  # both point to the same integer BUT when updating, creates new number at diff address

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# num1 and num2 point to the same address, the same number 11 in memory
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

print("--------------------------")
num2 = 22

# number 11 is still in the same place in memory. num2 is just pointing somewhere else in memory to 22
print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

print("--------------------------")
#####################################


dict1 = {
    'value': 11
}

dict2 = dict1   # both point to the same integer AND overrides number pointing to same address

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

print("--------------------------")

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
