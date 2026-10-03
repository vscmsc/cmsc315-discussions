# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

## Discussion Board Reflection

_Explain how traversal works and provide a real-world use case for breadth-first search or depth-first search. 
Describe when one is preferred over the other and why._

A Breadth-First Search (BFS) first visits a starting vertex and then works through the remaining vertices 
based on their distance from the starting vertex. This method branches outward during its search, 
visiting a graph level by level. In contrast, a Depth-First Search (DFS) follows one path as far as possible 
before returning and traversing the next available path. BFS is useful when looking for the 
shortest path between nodes and can be used in applications such as navigation systems. 
DFS can be useful for tasks such as cycle detection and analyzing dependencies or relationships. 
The choice between BFS and DFS depends on the structure of the problem and what information the traversal needs to find.

_Reflection on Skills, Concepts, and Challenges_

Learning how graphs can represent relationships in real-world applications helped me better understand why 
graph structures are useful beyond the examples in class. For this week's project, I felt that I 
understood the concepts behind BFS but then struggled with translating those concepts into code. 
One challenge during this post specifically was determining why I needed both `visited = set()` and `order = []`.
After trying to combine the two, my brain eventually pieced together their different purposes.
I ended up renaming `visited` to `discovered` in my own code because that distinction was easier for me to understand. 
Making that change helped clarify the purpose of each step and made the rest of the implementation easier.

