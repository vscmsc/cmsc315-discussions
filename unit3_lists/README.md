# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list (see `insert_at()`)
- Delete values from a list (see `delete_at()`)
- Search for values in a list (see by `search_value()`)
- Analyze list behavior and performance (see below)

## Requirements

1. Test insertion at the beginning, middle, and end.
* Before starting the tests, I initialized the list `character_inventory` with three items: Boots, Sword, and Helmet
I then used the `insert_at()` method to add items at the beginning and in the middle of the list.
To add an item at the end of the list, I used `len(character_inventory)` as the index.

2. Test deletion at the beginning, middle, and end.
* Similar to the tests for inserting values into the list, for the deletion tests I used the `delete_at()` method to remove items from the front and middle of the list.
To test deletion of an item from the end of the list, I used `len(character_inventory) - 1` as the index.

3. Search for existing and missing values.
* In these tests, I created if/else statements to print the results of the search.
In the test for the existing value, I also had it print the index where the value was found.

4. Demonstrate edge cases.
* The two edge cases tested were (1) deleting an item from an empty list, and (2) removing items from an invalid index. 
To test these, I created a new list `new_character_inventory` that was empty. 
I tested the deletion from an empty list first, which took some troubleshooting before ultimately working (detailed in Reflection below).
To test deletion from an invalid index, I added a few items and then attempted to delete a value from the index equal to the list's length.
Once I was calling the methods appropriately, both edge cases ran without causing program failure.

5. Create a real-world scenario.
* The `character_inventory` example could be used when going LARP-ing, 
or can be adjusted for packing for a trip (adding items during planning, inserting at locations to group by item type/location, and removing items once they've been packed), 
and even for creating grocery lists.

## Discussion Board Reflection

*What challenges did you encounter, and how did you overcome them?*
* The first edge case test I chose was to delete an item from an empty list. 
One thing about me and writing code is that I frequently struggle with remembering to actually use the methods I create. 
In the case of removing a value from an empty list, I was trying to manipulate the list directly in `main()` rather than calling on `delete_at()`.
This resulted in the validations I put in place being bypassed, and the program failing when I tried to delete a value from the empty list.
It took me a minute to realize that I wasn't _actually_ using `delete_at()` and was instead just trying to `.pop()` items out of the list.
After troubleshooting, I realized what I had done wrong and corrected my implementation of the program to actually _use_ the code I had written!


*How do list operations impact performance in real-world applications?*
* In real-world applications, list operations impact performance based on how frequently data is accessed, inserted, deleted, or searched.
The way a list is implemented will be based on the program's functions as well as users' needs.
Python lists and ArrayLists in Java provide fast random access based on indexed positions,
but inserting and deleting values from the list can be slow depending on where the operation occurs, since existing values will need to be shifted either left or right.

*What concepts or skills did you learn while completing this assignment?*
* Learning more about list manipulation and just getting more exposure to programming in general is always helpful.
  As discussed in the challenges section, a lot of what I learned came in the form of a reminder to myself to be more mindful about the code I'm writing and using.
  Working through this unit also helped me better understand the performance implications/considerations of lists.
