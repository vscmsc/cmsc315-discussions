# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

_Briefly explain your design approach and how your chosen application demonstrates the use of a hash table._

For this week’s assignment, I chose to use the example of a course catalog to 
demonstrate the use of a hash table through a Python dictionary. 
I created my course_catalog dictionary and added five courses to it, 
using course codes for the keys and full course titles for the values in my key-value pairs. 
For my edge cases, I chose to do three: searching for a missing key, 
attempting deletion of a missing key, and updating a missing key.

_Reflection on skills/concepts learned and challenges encountered_

Less of a ‘lesson learned’ and more of a ‘lesson remembered’, but the try-except block was definitely a more graceful approach to the 
KeyError handling than what I had initially been cobbling together. Week-to-week, one of the bigger challenges I end up 
having to overcome is swapping from Java to Python, and vice versa. It’s a minor thing, but finishing one assignment and 
getting a grasp on the concepts for the week in that programming language and then having to translate everything to the 
other programming language makes for a slow transition every week. This week in particular felt like more of a stretch than other weeks, 
especially when it came to working through the KeyError with a try-except block. That said, I’m grateful for the practice and 
mental exercise required by switching between the two, since my experience is still limited.

_Explain how hash tables behave, what collisions are (and how they impact performance), and how hash tables can improve efficiency._

Hash tables use hash functions to determine where key-value pairs should be stored. 
The key is passed through the hash function to identify an index or bucket where the pair can be stored. 
Because hash tables rely on algorithms rather than having to search all items sequentially 
(or use process of elimination, like with binary search trees), hash tables have an average 
time complexity of O(1) for operations such as searching, insertion, and deletion.

Collisions occur when the hash function identifies the same storage location for two different keys. 
Chaining and open-addressing are two of the collision resolution mechanisms that are used to handle collisions: 
chaining allows for multiple key-value pairs to be stored in the same bucket, and 
open-addressing searches for another available location (empty bucket) to store the key-value pair. 
Collisions impact performance because they mean additional time and resources are spent locating the key-value pair. 
Despite an average time complexity of O(1) for hash tables, their worst-case can be O(n) if many collisions occur.
