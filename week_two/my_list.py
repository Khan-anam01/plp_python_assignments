# 1. Create an empty list
my_list = []

# 2. Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)  # Output: [10, 20, 30, 40]

# 3. Insert value 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15:", my_list)  # Output: [10, 15, 20, 30, 40]

# 4. Extend the list with another list
my_list.extend([50, 60, 70])
print("After extending:", my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Remove the last element
my_list.pop()
print("After removing last element:", my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

# 6. Sort the list in ascending order
my_list.sort()
print("After sorting:", my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

# 7. Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)  # Output: 3