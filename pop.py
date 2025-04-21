# Example of using pop()
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# Pop the last item
last_item = numbers.pop()
print("Popped item:", last_item)
print("List after popping last item:", numbers)

# Pop item at index 1
second_item = numbers.pop(1)
print("Popped item at index 1:", second_item)
print("List after popping item at index 1:", numbers)

# Attempting to pop from an empty list
empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print("Error:", e)  # Will print an error message
