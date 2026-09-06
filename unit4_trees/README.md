# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

For this assignment, I chose to organize author names into a binary search tree. 
Using 10 author names in random order, I developed methods to insert values into a BST, search for a value in a BST, and print the values in-order. 
Each of these had recursive helper methods that performed the necessary work. 

Because I chose to use names and not numbers, I had to contend with the fact that string comparisons are case-sensitive by default. 
Since binary search trees sort based on whether values are greater/less than the current node's value, 
I added `.lower()` to my insertion and search methods to ensure that the comparisons were case-insensitive (while preserving the original values). 

___What concepts or skills did you learn while completing this assignment?___


Learning about BST's and how they can make large scale data processing challenges more efficient. 
I also gained a better understanding of recursion and how recursive helper methods can be used to navigate through a tree.


___What challenges did you encounter, and how did you overcome them?___

Recursion always tends to give my brain a workout, and this week was no exception. 
This was especially true when it came to the `_inorder_recursive()` method. 
Once it clicked that each recursive call was causing each node was performing each of those three lines of code independently 
(visiting the left subtree, then current node, then right subtree), things started to fall into place.


___Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.___

When searching for a target value, a linear search may have to check every item before it finds the target value. 
This results in a search time of _O(n)_.

On the other hand, a BST can be more efficient because it eliminates part of the remaining search space with each comparison. 
A balanced BST can have a search time of _O(log n)_, because each comparison can eliminate roughly half of the remaining values in a search space with each comparison made. 
However, the less balanced a BST is, the less efficient it is during a search. Worst case the tree looks like a stick, 
with each node only having one child. At that point it can also approach _O(n)_, similar to a linear search.