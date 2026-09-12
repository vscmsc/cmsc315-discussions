# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Discussion Board Reflection

For this assignment, I chose to use a database of ISBN numbers as my foundation. 
For the small dataset, I used ten ISBN numbers, and for the large dataset I generated 1,000 mock-ISBN numbers. 
For the large dataset, I did this by using a loop to append a new ISBN each time, 
incrementing the value by a set number each time. These are not valid ISBN numbers, 
but they worked for the purposes of this project.

My edge cases included searching an empty list and searching for the value at the first index. 
I also included one special case - searching for a duplicate value - to highlight how the 
returned index may differ depending on the search method used.

_Binary vs. Linear Search_

A linear search starts at index 0 and continues its search incrementally until the 
target is found or the end of the list is reached. 
In contrast, a binary search starts by checking the middle index of the current search space for the target value. 
If the value is not found at the middle index, the algorithm repeats the search on 
one of the two resulting halves, again starting from the middle.

In terms of performance, it’s easy to see why a binary search is more efficient than a linear search. 
When searching for a target value, a linear search may have to check every item before it 
finds the target value or reaches the end of the list, resulting in a runtime complexity of O(N). 
A binary search, on the other hand, has a maximum number of steps of log2 N + 1, 
because it effectively eliminates half of the remaining search values at each step. 
This means that if we have a list of 1,000 values, a linear search might have to search all 1,000 
values if the target is the last value or is not present, whereas the maximum number of comparisons 
performed on the same dataset by a binary search would only be around 11.

Despite this performance difference, linear searches can still be an appropriate choice 
when it comes to small or unsorted datasets. Binary searches rely on data being sorted, 
and so a binary search can’t be used on such datasets (unless you sort the data first). 
For example, consider searching for a word within the text of a webpage. 
The words aren't organized alphabetically, so a simple search through the text 
cannot take advantage of binary search's requirement for sorted data.

_Reflection on skills/concepts learned and challenges encountered_

Overall, I learned a lot this week about these two types of search methods, 
and what situations they are appropriate for. In terms of challenges, 
I had a weirdly hard time implementing the binary search code in this project and the lab. 
What helped was just remembering that there are many examples available to us in our textbook, 
and to see how it was implemented there, understand it, and translate it to Python.  
(Also silly me - I got a head start last weekend and forgot a lot of what I had learned from the lab 
when it came time to work on the discussion project.)
