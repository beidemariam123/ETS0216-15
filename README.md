# first commit (tuple methods)
1. count(value)

• Purpose: The count() method is used to determine how many times a specific value appears in a tuple.

• Syntax:
tuple.count(value)

• value: The value you want to count in the tuple.

• Return Value: This method returns an integer representing the number of occurrences of the specified value.

Example:
    my_tuple = (1, 2, 3, 2, 4)

    # Count how many times '2' appears in the tuple
    count_of_two = my_tuple.count(2)  
    print(count_of_two)  # Output: 2

    # Count how many times '5' appears in the tuple
    count_of_five = my_tuple.count(5)  
    print(count_of_five)  # Output: 0

2. index(value[, start[, end]])

• Purpose: The index() method is used to find the first occurrence of a specified value within a tuple. You can also specify optional start and end indices to limit the search to a specific section of the tuple.

• Syntax:
tuple.index(value[, start[, end]])

• value: The value you want to find the index of.

• Return Value: This method returns the index of the first occurrence of the specified value. If the value is not found, it raises a ValueError.

Example:
    my_tuple = (1, 2, 3, 2, 4)

    # Find the index of the first occurrence of '3'
    index_of_three = my_tuple.index(3)  
    print(index_of_three)  # Output: 2

    # Find the index of '2', starting the search from index 3
    index_of_two_after_index_3 = my_tuple.index(2, 3)  
    print(index_of_two_after_index_3)  # Output: ValueError, because '2' does not appear after index 3

