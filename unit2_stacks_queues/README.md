# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

1. Implement stack operations.
   * `__init__` initializes a list named stack_items, which is used as the internal data structure for implementing stack/LIFO behavior.
   * `push()` adds values to the stack using `.append()`. This operation supports LIFO behavior by adding the value to the "top" of the stack. 
   * `pop()` removes and returns the item last "pushed" to the stack. It first checks for whether the stack is empty, returning a message indicating the error if it is.
   * `peek()` returns the value at the top of the stack *without* removing it. In Python, this is done using `return self.stack_items[-1]`. This method also checks for an empty list, returning an error message if it is empty.
   * `is_empty()` allows us to perform the empty-checks in the previous methods. If the length of `stack_items` is 0, it returns True, otherwise it returns False.


2. Implement queue operations.
   * `__init__` initializes a deque named queue_items, which is used as the internal data structure for implementing queue/FIFO behavior. Using `deque` allows us to add/remove values from both the front and the back.
   * `enqueue()` adds values to the "back" of the queue using `.append()`. This supports FIFO behavior by mimicking a line or a queue.
   * `dequeue()` removes the value from the "front" of the queue using `.popleft()`. This is a feature of deque. This method first checks for whether the queue is empty, returning a message indicating the error if it is. 
   * `front()` fills the role of peek, returning the value at the front of the queue *without* removing it. This is done using `return self.queue_items[0]`. This method also checks for whether the queue is empty, returning a message indicating the error if it is.
   * `is_empty()` as with the previous implementation, this method allows us to perform the empty-checks in the other methods. If the length of `queue_items` is 0, it returns True, otherwise it returns False.


3. Demonstrate LIFO behavior.
    * To demonstrate LIFO behavior, I used a real-life example of going on a hike to demonstrate last-in, first-out (LIFO) behavior. 
   Using print statements throughout, I told a story of a hiker passing through four checkpoints.
   Each checkpoint passed was added to the stack in the order it was passed.
   On the way back down, the checkpoints were popped from the stack in reverse order, demonstrating how the last item added to the stack becomes the first one out of the stack.


4. Demonstrate FIFO behavior.
    * To demonstrate FIFO behavior, I used the real-world example of airplane boarding.
   In this example, passengers queued up to board based on their boarding group: Group 1, Group 2, Group 3, or Group 4.
   The first group called (the first group in the queue) is able to board first; 
   in other words, the first to enter the queue is the first to leave the queue.


5. Create and test edge cases.
    * Both the Stack (LIFO) and Queue (FIFO) demos include the following edge case tests:
      * Show what happens when `pop()` or `dequeue()` are used on an empty stack/queue.
      * Show what happens when `peek()` or `front()` are used on an empty stack/queue.
    * Each demo also includes a section where a stack/queue is created, one item is added and then removed, and the stack/queue is shown to be empty again at the end.
    * I also included a one-off, mid-run `peek()` or `front()` to demonstrate how these methods simply return the top or front item without changing anything.


6. Create a real-world scenario.
    * Both of my demos demonstrate real-world examples for LIFO and FIFO behavior: 
      * Stack/LIFO: A hiker passes four checkpoints on a short out-and-back hike. When the hiker makes the return trip, they pass the checkpoints in reverse order. 
        At one point, the hiker checks their map to see the last checkpoint they passed, demonstrating how `peek()` functions.
      * Queue/FIFO: A flight is boarding in order of the groups called to queue. The first group to queue is the first group that is allowed to board the plane.
        In the example, the desk agent loses track of the boarding process and has to check her notes to see who is next in the queue, demonstrating how `front()` functions.


## Discussion Board Reflection

*Briefly explain your design approach and how your chosen application scenario demonstrates the use of the data structure.*
* Truly, having the road map of requirements is such a huge benefit in these units. 
It’s easy to keep track of what still needs to be done, and leaves more brainpower for troubleshooting – 
and it also left me with the capacity to get carried away with the story-telling aspect of my hiker (in Stack/LIFO demo) and desk agent (in Queue/FIFO demo). 
In terms of the use of data structures, the Stack uses a list, with append() adding to the top and pop() then removing from the top. 
It’s a simple way to implement a stack in Python. On the other hand, Queue used a deque, which allows for items to be inserted and removed at both the front and back. 
Here we used append() again to add to the back, and popleft() is used to remove the item at the front. This mimics queuing functionality.

*Briefly explain theoretically how much memory your structure uses as it grows (e.g., does it store more data as more items are added?).*
* Both my stack and my queue are unbounded in the sense that I did not specify a maximum length. 
This means that the more items that are added, the more memory is required to store those items. 
It can’t actually grow indefinitely since computers have finite memory, but allowing the structures to grow without a defined limit could eventually cause memory issues if not handled properly.

*What concepts or skills did you learn while completing this assignment?*
* Throughout this unit I learned much more about stacks and queues than I think I ever knew in the first place, and it was nice getting hands-on practice working with these different data structures. 
Working through the examples in this unit also helped me understand that the structures aren’t just about storing data, but the way we add/remove values also determines the behavior of the structure.

*What challenges did you encounter, and how did you overcome them?*
* One thing that caught me up was actually implementing some of these in Python (e.g. peek()). 
Learning (or possibly re-learning) how to add, remove, and return values from the list was something I definitely needed. 
Another issue I had was with my error handling, and returning the proper values. I initially had issues due to printing the error message and then returning, rather than just returning the error message as a string.

*Explain the differences between stacks and queues as this relates to real-world applications.*
* Stacks exhibit last-in, first-out (LIFO) and are useful where the last item added is the first one that needs to be processed. 
This is akin to the way you stack pieces of paper: you place one piece on top of another on top of another (and so on), 
and the only way to get to the paper you placed lower in the stack is by removing the pieces from the top to get to what’s underneath. 
In this case, the last item in (the last piece of paper placed on the pile) must be removed to get to what’s underneath.
* Queues exhibit first-in, first-out (FIFO) behavior and are useful when the first item that was added should be the first item that is processed. 
This is much like queuing in a line at the grocery store: the first person that gets in line is the first person to scan, pay, and eventually come out the other side of the line.