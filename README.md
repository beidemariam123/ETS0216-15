# first commit (dictionary methods)

1. dict.clear()

•  Purpose: Removes all items from the dictionary.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    my_dict.clear()
    # my_dict is now {}

2. dict.copy()

•  Purpose: Returns a shallow copy of the dictionary.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    new_dict = my_dict.copy()
    # new_dict is {'a': 1, 'b': 2}

3. dict.fromkeys(iterable, value=None)

•  Purpose: Creates a new dictionary from the given iterable, with keys from the iterable and values set to the specified value (default is None).

•  Example:

    keys = ['a', 'b', 'c']
    new_dict = dict.fromkeys(keys, 0)
    # new_dict is {'a': 0, 'b': 0, 'c': 0}

4. dict.get(key, default=None)

•  Purpose: Returns the value for the specified key if it exists; otherwise, returns the default value.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    value = my_dict.get('c', 0)  # Returns 0 since 'c' is not in the dictionary

5. dict.items()

•  Purpose: Returns a view object that displays a list of a dictionary's key-value tuple pairs.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    items = my_dict.items()  # Returns dict_items([('a', 1), ('b', 2)])

6. dict.keys()

•  Purpose: Returns a view object that displays a list of all the keys in the dictionary.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    keys = my_dict.keys()  # Returns dict_keys(['a', 'b'])

7. dict.pop(key, default=None)

•  Purpose: Removes the specified key and returns its value. If the key is not found, it returns the default value if provided; otherwise, it raises a KeyError.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    value = my_dict.pop('a')  # value is 1; my_dict is now {'b': 2}

8. dict.popitem()

•  Purpose: Removes and returns an arbitrary (key, value) pair from the dictionary. Raises KeyError if the dictionary is empty.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    item = my_dict.popitem()  # item could be ('a', 1) or ('b', 2)

9. dict.update([other])

•  Purpose: Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.

•  Example:

    my_dict = {'a': 1}
    my_dict.update({'b': 2, 'c': 3})
    # my_dict is now {'a': 1, 'b': 2, 'c': 3}

10. dict.values()

•  Purpose: Returns a view object that displays a list of all the values in the dictionary.

•  Example:

    my_dict = {'a': 1, 'b': 2}
    values = my_dict.values()  # Returns dict_values([1, 2])

11. dict. setdefault()

•  Purpose: The setdefault() method in Python dictionaries is used to retrieve the value of a specified key. If the key does not exist, it inserts the key with a specified default value. This method is useful for initializing dictionary keys without having to check if they already exist.

•  Example

# List of items
items = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'banana']

# Counting occurrences using setdefault()
item_count = {}
for item in items:
    item_count.setdefault(item, 0)  # Initialize count to 0 if not present
    item_count[item] += 1            # Increment the count

print(item_count)  # Output: {'apple': 2, 'banana': 3, 'orange': 2}


