"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # This for loop will iterate through the list until
    # it either finds its target or it searches all indexes.
    # Linear search has O(n) time complexity because it
    # may need to search all list elements before terminating
    # (this would be the worst case).
    for i in range(len(lst)):
        if lst[i] == target:
            # If the target is found, the index of the target is returned.
            return i

    # If the target is not found, -1 will be returned
    return -1



def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Initializing low and high as the first index (0) and last index (length - 1)
    low = 0
    high = len(lst) - 1

    # Creating a while loop to work through the list
    # As stated above, this assumes the list is already sorted
    # This search continuously splits the remaining search space in half
    # by finding the midpoint, comparing it to the target,
    # and adjusting the low/high variables to shift the search space accordingly
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < target:
            # if the mid-point is less than the target, the search should continue to the "right"
            # hence, the new "low" should be one index to the right of the mid-point
            low = mid + 1
        elif lst[mid] > target:
            # if the mid-point is higher than the target, the search should continue to the "left"
            # hence, the new "high" should be one index to the left of the mid-point
            high = mid - 1
        else:
            return mid

    # If the target is not found, return -1
    # This also handles an empty list, since low would be greater than high
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Initializing a list with 10 'ISBN-13' numbers
    small_dataset = [9780061120084, 9780141439518, 9780141439556, 9780141439600, 9780142437247,
                     9780307474278, 9780451524935, 9780451526342, 9780553213102, 9780743273565]

    """Linear Search Tests"""

    print("\nLinear Search Results:")
    # Searching for a value that exists
    # Expected result is 3, since the value 9780141439600 is located at index 3
    print("\tSearching for a number that exists: ", linear_search(small_dataset, 9780141439600))
    # Searching for a value that does not exist
    # Expected result is -1, since the target will not be found
    # while the algorithm works through the list
    print("\tSearching for a number that does not exist: ", linear_search(small_dataset, 9780000011118))

    """Binary Search Tests"""

    print("\nBinary Search Results:")
    # As with the linear search (and since we searched the same value),
    # the expected result when searching for the value 9780141439600 is 3,
    # since the value is located at index 3
    print("\tSearching for a number that exists: ", binary_search(small_dataset, 9780141439600))
    # Likewise, the expected result when searching for the value 9780000011118 is -1,
    # since the target was not found while algorithm worked through the list.
    print("\tSearching for a number that does not exist: ", binary_search(small_dataset, 9780000011118))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Filling the list with 1,000 mock-ISBN numbers
    # Because this is only meant to simulate a large dataset of ISBNs, these are obviously NOT valid ISBNs
    large_dataset = []
    i = 0
    isbn = 9780141439518
    while i < 1000:
        large_dataset.append(isbn)
        # To keep it simple in generating the mock-ISBN numbers, I chose to add a set number to each previous value.
        isbn += 123456
        # Incrementing i by 1 so the loop does not run indefinitely
        i += 1



    print("\nLinear Search Results:")
    # Searching for a value that exists
    # Expected result is 912, since the value 9780254031390 is located at index 912
    print("\n\tSearching for a value that exists: ", linear_search(large_dataset, 9780254031390))
    # Searching for a value that does not exist
    # Expected result is -1, since the target 9780000011118 will not be found
    # while the algorithm works through the list
    print("\tSearching for a value that does not exist: ", linear_search(large_dataset, 9780000011118))

    print("\nBinary Search Results:")
    # As with the linear search (and since we searched the same value),
    # the expected result when searching for the value 9780254031390 is 912,
    # since that value is located at index 912
    print("\n\tSearching for a value that exists: ", binary_search(large_dataset, 9780254031390))
    # Likewise, the expected result when searching for the value 9780000011118 is -1,
    # since the target was not found while algorithm worked through the list.
    print("\tSearching for a value that does not exist: ", binary_search(large_dataset, 9780000011118))

# ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE/SPECIAL CASE TESTS ===")
    print("TODO: Demonstrate and explain edge/special cases.")

    # Not really an edge case, but certainly a special case: duplicate values
    # Because of how linear and binary searches are performed, there is a chance that
    # the returned index may be different even when searching for the same value.
    print("\n* * Special Case: Searching Duplicate Values * *")
    print("\nIf duplicate values ended up on the list, the returned index may be different depending on the type of search.")

    # Initializing a list with duplicate entries / printing to screen
    dupe_list = [9780061120084, 9780141439518, 9780141439556, 9780141439600, 9780141439600,
                 9780141439600, 9780142437247, 9780307474278, 9780451524935, 9780451526342]
    print("\nFor example, take the following list of ISBNs: ")
    print(dupe_list)

    # Calling the methods/printing the output
    print("\nUsing a linear search, the index returned is - ", linear_search(dupe_list, 9780141439600), " - when searching for 9780141439600.")
    print("Using a binary search, the index returned is - ", binary_search(dupe_list, 9780141439600), " - when searching for 9780141439600.")

    # Explanation of linear vs. binary searches, why results might differ
    print("\nThe returned indices are different due to how linear vs. binary searches are performed.")
    print("A linear search starts at index 0 and continues its search incrementally until the target is found or the end of the list is reached.")
    print("In contrast, a binary search starts by checking the middle index of the current search space for the target value.")
    print("If the value is not found at the middle index, the algorithm repeats the search on one of the two resulting halves, again starting from the middle.")
    print("Because of this, a binary search is not guaranteed to find the first instance of a value, ultimately resulting in different index values for the value targeted.")

    # Testing the ability to find the value at the first index
    print("\n* * Edge Case: Searching for the Value at First Position * *")

    # Calling the methods/printing the output
    print("\nSearching for the first position value using linear search: ", linear_search(small_dataset, 9780061120084))
    print("Searching for the first position value using binary search: ", binary_search(small_dataset, 9780061120084))

    # Explanation of the different steps the linear/binary searches took to find the target value
    print("\nBoth searches find the value at the first index.")
    print("However, due to the way binary and linear searches are performed, "
          "\nthe linear search returns the index on its first comparison, "
          "\nwhereas the binary search goes through multiple iterations "
          "\nbefore finding the target value.")

    # Testing the ability to handle empty lists
    print("\n* * Edge Case: Searching an Empty List * *")

    # Initializing our empty list
    empty_list = []

    # Calling the methods/printing the output
    print("\nSearching an empty list using linear search returns: ", linear_search(empty_list, 9780141439600))
    print("Searching an empty list using binary search returns: ", binary_search(empty_list, 9780141439600))

    # Explanation of what was returned, significance of -1
    print("\nSearching an empty list with both the linear and binary search methods "
          "\ncorrectly returned -1, since there are no elements to search.")


if __name__ == "__main__":
    main()