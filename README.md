# first commit (set methods)

1. set.add(element)

•  Explanation: The add() method adds a single element to the set. If the element is already present in the set, the set remains unchanged (sets do not allow duplicate elements).

•  Purpose: To add a new element to a set, ensuring uniqueness.

•  How it Works:

  1. The method checks if the element is already present in the set.
  2. If the element is not present, it is added to the set.
  3. If the element is already present, the set remains unchanged.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)  # Output: {1, 2, 3, 4}

    my_set.add(2)  # Adding an existing element has no effect
    print(my_set)  # Output: {1, 2, 3, 4}

2. set.remove(element)

•  Explanation: The remove() method removes a specified element from the set. If the element is not found in the set, it raises a KeyError.

•  Purpose: To remove a specific element from a set.

•  How it Works:

  1. The method checks if the element is present in the set.
  2. If the element is present, it is removed.
  3. If the element is not present, a KeyError is raised.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.remove(2)
    print(my_set)  # Output: {1, 3}

    try:
        my_set.remove(4)  # Raises KeyError
    except KeyError:
        print("Element not found")

3. set.discard(element)

•  Explanation: The discard() method removes a specified element from the set if it is present. Unlike remove(), it does not raise an error if the element is not found; it simply does nothing.

•  Purpose: To remove an element from a set without worrying about whether it exists. This provides a safer way to remove elements compared to remove().

•  How it Works:

  1. The method checks if the element is present in the set.
  2. If the element is present, it is removed.
  3. If the element is not present, the set remains unchanged.

•  Example (Python):

    my_set = {1, 2, 3}
    my_set.discard(2)
    print(my_set)  # Output: {1, 3}

    my_set.discard(4)  # No error is raised
    print(my_set)  # Output: {1, 3}

4. set.pop()

•  Explanation: The pop() method removes and returns an arbitrary element from the set. Because sets are unordered, you cannot predict which element will be removed. If the set is empty, calling pop() raises a KeyError.

•  Purpose: To remove and retrieve an element from a set when the specific element doesn't matter.

•  How it Works:

  1. If the set is empty, a KeyError is raised.
  2. Otherwise, an arbitrary element is removed from the set.
  3. The removed element is returned.

•  Example (Python):

    my_set = {1, 2, 3}
    element = my_set.pop()
    print(f"Removed element: {element}")
    print(f"Updated set: {my_set}")

    try:
        empty_set = set()
        empty_set.pop()  # Raises KeyError
    except KeyError:
        print("Set is empty")