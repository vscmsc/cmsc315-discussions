"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""
import copy


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # Creating a copy of the original list
    lst_copy = copy.deepcopy(lst)

    # Storing the length of the list
    n = len(lst_copy)

    # Returning if list is empty
    if n < 1:
        return lst_copy

    # Using nested loops to implement the bubble sort
    for i in range(n):
        # Flag to catch if a swap occurred or not
        swapped = False
        # Comparing the neighboring values
        # At each pass, the largest unsorted value moves toward the end of the list
        # Using n - i - 1 (rather than just n - 1) avoids checking the values that have already been sorted
        for j in range(0, n-i-1):
            # Checking to see if the current element is larger than the element to its right
            if lst_copy[j] > lst_copy[j + 1]:
                # If it is, swaps their order
                lst_copy[j], lst_copy[j + 1] = lst_copy[j + 1], lst_copy[j]
                # Indicates a swap occurred
                swapped = True
        # If no swaps occurred in this pass, stop early
        if not swapped:
            break
    # Returns the sorted list
    return lst_copy


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """

    # If a list is empty or if it contains 1 element it is already sorted,
    # so there is nothing left to divide or sort (return)
    if len(lst) <= 1:
        return lst

    # Finding the midpoint and dividing into two smaller halves
    # Merge sort continues dividing these halves recursively until
    # each list contains 0 or 1 element.
    mid_index = len(lst) // 2
    left_half = lst[:mid_index]
    right_half = lst[mid_index:]

    # Recursively sorting each half
    # Each call continues until it reaches the either 0 or 1 element
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Once both halves are sorted, merge into one sorted list
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    # Creating the list to hold the sorted values
    merged_list = []
    # Initializing i and j to keep track of left (i) and right (j) positions
    i = j = 0

    # Compare the smallest remaining value from each sorted half
    # Each half is already sorted, so the smaller of the two is the
    # next value appended to the merged list.
    while i < len(left) and j < len(right):
        # If the left value is smaller, append it to the merged list and
        # move to the next value in the left list (increment i by 1).
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        # Otherwise, append the right value to the merged list and
        # increment the right counter (j) by 1.
        else:
            merged_list.append(right[j])
            j += 1

    # While there are still values remaining in the left list,
    # append them to the merged list.
    # Because they are already sorted, they can be added directly.
    while i < len(left):
        merged_list.append(left[i])
        i += 1

    # While there are still values remaining in the right half,
    # append them to the merged list.
    # Because they are already sorted, they can be added directly.
    while j < len(right):
        merged_list.append(right[j])
        j += 1

    # Return the sorted list
    return merged_list


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # Creating an unsorted list of product prices
    price_list = [5.25, 18.75, 25.45, 60.6, 45.2, 55, 20.7, 35, 43.8, 85]

    # Displaying the unsorted list of prices, both unformatted and formatted
    print("\nThe (unformatted) unsorted list of prices: ", price_list)
    print("The (formatted) unsorted list of prices: " + ", ".join(f"${price:.2f}" for price in price_list))

    # Creating a list to store the bubble sorted values
    # Displaying the list after using bubble_sort()
    bubble_sorted = bubble_sort(price_list)
    print("After using bubble_sort(): " + ", ".join(f"${price:.2f}" for price in bubble_sorted))

    # Creating a list to store the merge sorted values
    # Displaying the list after using merge_sort()
    merge_sorted = merge_sort(price_list)
    print("After using merge_sort(): " + ", ".join(f"${price:.2f}" for price in merge_sorted))


# ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    sale_prices = []
    n = len(price_list)
    for i in range(n):
        # Generating sale prices (30% off) to generate the second dataset
        # Resulting prices are stored in a separate list
        sale_prices.append(round(price_list[i] * .7, 2))

    # Displaying the unsorted list of prices, both unformatted and formatted
    # (Although yes, I rounded when I generated the second dataset! Unformatted except for that...)
    print("\nThe (unformatted) unsorted list of sale prices: ", sale_prices)
    print("The (formatted) unsorted list of sale prices: "+ ", ".join(f"${price:.2f}" for price in sale_prices))

    # Creating a list to store the bubble sorted values
    # Displaying the list after using bubble_sort()
    bubble_sorted_sales = bubble_sort(sale_prices)
    print("After sorting with bubble_sort(): "+ ", ".join(f"${price:.2f}" for price in bubble_sorted_sales))

    # Creating a list to store the merge sorted values
    # Displaying the list after using merge_sort()
    merge_sorted_sales = merge_sort(sale_prices)
    print("After sorting with merge_sort(): "+ ", ".join(f"${price:.2f}" for price in merge_sorted_sales))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Empty list

    # Creating our empty list
    empty_list = []

    # Calling both bubble_sort() and merge_sort()
    # Neither breaks, since we added a check for empty lists to both methods.
    # bubble_sort() checks whether the list length is less than 1 and returns the empty copy.
    # merge_sort() uses its len(lst) <= 1 base case and returns the empty list without actioning it.
    print("\nEmpty list edge case: ")
    print("List used for this edge case: ", empty_list)
    print("After bubble_sort(empty_list): ", bubble_sort(empty_list))
    print("After merge_sort(empty_list): ", merge_sort(empty_list))

    # Edge case 2: Sorted list

    # Creating the sorted list
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Nothing specific happens here visually because the list is already sorted,
    # however, bubble_sort() uses a 'swapped' flag to check whether a swap occurred.
    # Because no values were swapped (the list is already sorted),
    # the method would have ended early and not performed the remaining passes.
    # Merge sort does not have the same early-exit check,
    # so it still divides/merges the list even though it is already sorted.
    print("\nSorted list edge case: ")
    print("List used for this edge case: ", sorted_list)
    print("After bubble_sort(sorted_list): ", bubble_sort(sorted_list))
    print("After merge_sort(sorted_list): ", merge_sort(sorted_list))

if __name__ == "__main__":
    main()