listA = [4, 2, 6, 5, 1, 3]

print(listA)
print()


print("======================== 1 ========================")
print("len(listA):\t\t\t\t\t\t", len(listA))
print()


print("======================== 2 ========================")
print("range(len(listA)):\t\t\t\t", range(len(listA)))
print()


print("======================== 3 ========================")
print("range(len(listA) - 1):\t\t\t", range(len(listA) - 1))
print()


print("======================== 4 ========================")
for i in range(len(listA)):
    print("range(len(listA)):\t\t\t\t i at", i, "is", listA[i])
print()


print("======================== 5 ========================")
for i in range(len(listA) - 1):
    print("range(len(listA) - 1):\t\t\t i at", i, "is", listA[i])
print()


print("======================== 6 ========================")
for i in range(len(listA) - 1, 0, -1): 
    print("range(len(listA) - 1, 0, -1):\t i at", i, "is", listA[i])