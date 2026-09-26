# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

For this week’s assignment, I used a price list for my first dataset (price_list), and generated a sale price list by 
applying a “30% off” discount to each value in the original list to create my second dataset (sale_prices). 
For my edge cases, I chose to demonstrate calling the methods with an empty list and with an already sorted list.

_Bubble Sort vs. Merge Sort_

Bubble sort compares adjacent elements and swaps their positions if the first element is greater than the second element.
It uses nested loops, with the outer loop iterating N - 1 times (given N elements in the array). 
The inner loop handles the neighbor comparisons, gradually pushing the largest unsorted value to the end of the array (the highest index). 
Each pass through the array pushes the largest remaining value to its correct index, until eventually 
every value is placed in ascending order. Bubble sort has a runtime complexity of O(N2) and is generally 
less practical for real-world applications because many more efficient sorting algorithms exist. 
However, with the early-exit condition implemented in the bubble_sort() method, bubble sort can stop 
before completing all of its passes if no swaps occur during a pass. This makes it efficient for lists that are already or nearly sorted.
Merge sort works by repeatedly dividing a list into smaller halves and recursively sorting each half 
until each half contains only one element, since a single-element list is already sorted. 
It then merges these sorted pieces back together to produce one sorted list. It does this by comparing the smallest remaining value 
from each half, then adding the smaller value to the merged list. Once all the values have been compared 
(and any remaining values have been added, the merged list is returned. Merge sort has a runtime complexity of O(N log N), 
and as such is considered a fast sorting algorithm. It is generally more efficient than bubble sort, especially for larger datasets.

_Reflection on Skills, Concepts, and Challenges_

The edge case for the already sorted list helped drive home the efficiency comparison between bubble sort and merge sort. 
Because my implementation of bubble sort had the early-exit, it would have completed faster than merge sort, 
which still had to “divide and conquer” its way through the list and doesn’t have the luxury of an early exit. 
However, it’s also easy to see how merge sort’s “divide and conquer” approach 
(much like our previous discussion around binary search methods and BSTs) would be more efficient for larger/unsorted datasets.

Overall, nested loops/recursion are still a weak point for me, but I’m grateful for each iteration (ha) 
that helps reinforce these concepts.
