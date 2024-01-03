# Creating a dictionary
my_dict = {'name': 'Wahib', 'age': 25, 'city': 'Taiz', 'gender': 'Male'}

# Displaying the original dictionary
print("Original Dictionary:", my_dict)

# 1. Accessing values using keys
print("1. Accessing values using keys:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# 2. Getting all keys and values
print("\n2. Getting all keys and values:")
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", keys)
print("Values:", values)

# 3. Getting items (key-value pairs)
print("\n3. Getting items (key-value pairs):")
items = my_dict.items()
print("Items:", items)

# 4. Modifying a value
print("\n4. Modifying a value:")
my_dict['age'] = 26
print("Modified Dictionary:", my_dict)

# 5. Adding a new key-value pair
print("\n5. Adding a new key-value pair:")
my_dict['occupation'] = 'Engineer'
print("Updated Dictionary:", my_dict)

# 6. Removing a key-value pair using pop
print("\n6. Removing a key-value pair using pop:")
removed_value = my_dict.pop('gender')
print("Removed value:", removed_value)
print("Updated Dictionary:", my_dict)

# 7. Removing a key-value pair using popitem
print("\n7. Removing a key-value pair using popitem:")
removed_item = my_dict.popitem()
print("Removed item:", removed_item)
print("Updated Dictionary:", my_dict)

# 8. Clearing the dictionary
print("\n8. Clearing the dictionary:")
my_dict.clear()
print("Cleared Dictionary:", my_dict)
