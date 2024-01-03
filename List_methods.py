# Original list
L = [1, 1, 2, 3, 4, 5, 6]
# Tuple to be converted to a list
T = (8, 9, 10)

# Displaying information about the original list
print("Size of the list:", len(L))
print("Max element in the list:", max(L))
print("Min element in the list:", min(L))

# Converting tuple to a list
L2 = list(T)
print("Change the tuple to a list:", L2)

# Appending an element to the original list
L.append(20)
print("Add 20 to the list:", L)

# Counting occurrences of the number 1 in the list
print("How many times the number 1 is found in the list:", L.count(1))

# Extending the original list with elements from a new tuple
New_T = (21, 22)
L.extend(New_T)
print("Add a new tuple to the old list:", L)
print("The tuple that was added to the list:", New_T)

# Finding the index of the element 3
print("Index of the element 3:", L.index(3))

# Inserting the element 55 at index 2
L.insert(2, 55)
print("Add 55 to the 2nd index:", L)

# Removing and displaying the element at index 2
deleted_element = L.pop(2)
print("Removed element:", deleted_element)
print("Updated List:", L)

# Removing and displaying the last element
deleted_element = L.pop()
print("Updated List (last element popped):", L)

# Removing the element 20 from the list
L.remove(20)
print("Updated List (element 20 removed):", L)

# Reversing the order of elements in the list
L.reverse()
print("Updated List (reversed):", L)

# Sorting the list in ascending order
L.sort()
print("Updated List (sorted in ascending order):", L)
