# List of items
items = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'banana']

# Counting occurrences using setdefault()
item_count = {}
for item in items:
    item_count.setdefault(item, 0)  # Initialize count to 0 if not present
    item_count[item] += 1            # Increment the count

print(item_count)  # Output: {'apple': 2, 'banana': 3, 'orange': 2}