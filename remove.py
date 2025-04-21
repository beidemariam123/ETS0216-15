# Example of using remove()
fruits = ['apple', 'banana', 'cherry', 'banana']
print("Original list:", fruits)

# Remove 'banana' from the list
fruits.remove('banana')
print("List after removing 'banana':", fruits)

# Attempting to remove a non-existent item
try:
    fruits.remove('orange')
except ValueError as e:
    print("Error:", e)  # Will print an error message
