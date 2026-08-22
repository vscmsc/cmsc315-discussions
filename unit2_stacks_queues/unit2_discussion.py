"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Creating the internal data structure (list) for our stack
        self.stack_items = []


    def push(self, value):
        # TODO (Student): Add value to the stack.
        # This operation supports Last-In, First-Out behavior by adding the value to the top of the stack
        # The most recent value appended will be the first one to be removed with pop(), or viewed with peek()
        self.stack_items.append(value)


    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # First checking to see if the stack is empty
        if self.is_empty():
            # If the stack is empty, print an error and return
            return "The stack is empty, nothing to pop!"
        # Otherwise, remove and return the most recently added value
        else:
            return self.stack_items.pop()


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek returns the top value of the stack without removing it
        # First checking to see if the stack is empty
        if self.is_empty():
            # If the stack is empty, print an error and return
            return "The stack is empty, nothing to peek!"
        # Otherwise, return the most recently added value
        else:
            return self.stack_items[-1]    # Returns the top item in Python lists

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Checking whether the length of our list stack_items is 0
        # Returns True if yes, False if no
        if len(self.stack_items) == 0:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Creating our internal data structure for the Queue class
        # Using deque allows for items to be inserted/removed at both the front and back
        # This allows for us to remove values from the front of the "queue" while adding values to the back/end
        self.queue_items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Using .append to add a value to the back of the queue
        # This operation supports FIFO behavior by mimicking a "line" or "queue"
        # Values get added to the end, while being removed from the front
        self.queue_items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # First checking to see if the queue is empty
        # If so, print an error and return
        if self.is_empty():
            return "The queue is empty, nothing to dequeue!"
        # Otherwise, uses .popleft() to remove and return the value from the front of the queue
        else:
            return self.queue_items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # First checking to see if the queue is empty
        if self.is_empty():
            # If it is, print an error and return
            return "The queue is empty, nothing to show!"
        # Otherwise, front() will return the first item in the queue (the oldest item added) without removing it
        else:
            return self.queue_items[0]    # Used by deque to show the first item

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Checking whether queue_items is empty
        # Returns True if yes, returns False if no
        if len(self.queue_items) == 0:
            return True
        else:
            return False


def main():

    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    # Commented out the printed requirements:
        # print("\n=== STACK DEMO ===")
        # print("TODO: Create a Stack object, demonstrate LIFO behavior,")
        # print("      test popping from an empty stack,")
        # print("      test peeking at an empty stack,")
        # print("      and verify a single-item stack becomes empty after removal.")

    print("\n=== STACK DEMO: A Short Hike ===")

    # Creating the Stack object short_hike to represent a short out-and-back hike
    # The hike checkpoints demonstrate LIFO behavior
    short_hike = Stack()

    # Print statements for commentary
    print("\nThis demo uses the idea of a short out-and-back hike to demonstrate LIFO behavior.")
    print("\nThe hiker passes the following checkpoints on the way to the peak:")

    # Adding four hike checkpoints to the stack
    short_hike.push("Community Center")
    short_hike.push("Old Creek Path")
    short_hike.push("Outlook Cliff")
    short_hike.push("Hawk Peak")

    # Printing the current stack contents
    print(f"    {'\n    '.join(short_hike.stack_items)}")

    # Throwing in a mid-run peek() to demonstrate that it returns the top value without removing it
    print("\nAt the rest area, the hiker forgot what checkpoint they just passed, so they peek at their map.")
    print("Ah-ha! They just passed " + short_hike.peek() + "!")

    print("\nOn the way back, those checkpoints are passed in reverse order:")

    # "pop"-ing from the stack to show the LIFO behavior
    while not short_hike.is_empty():
        popped = short_hike.pop()
        print("    " + popped)

    # Demonstrating what happens when you pop and peek an empty stack
    print("\nWhen there are no items in the stack, pop() returns: " + short_hike.pop())
    print("\nWhen there are no items in the stack, peek() returns: " + short_hike.peek())

    # Create a stack with only one item, remove it, and verify the stack is empty afterward
    # str(len(sample_stack.stack_items)) used to dynamically fill the number of items in the stack after the push/pop operations
    sample_stack = Stack()    # initiating the sample_stack stack
    print("\nAs one more example, we've created a new stack. It currently has " + str(len(sample_stack.stack_items)) + " items.")
    sample_stack.push("Hat")    # pushing an item onto the stack
    print("After adding an item, the new stack contains " + str(len(sample_stack.stack_items)) + " item: " + sample_stack.peek())
    print("Next, we will remove that item from our stack.")
    sample_stack.pop()    # popping the item off the stack
    print("Now, our stack contains " + str(len(sample_stack.stack_items)) + " items and is once again empty.")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    # Commented out the printed requirements:
        # print("\n=== QUEUE DEMO REQUIREMENTS ===")
        # print("TODO: Create a Queue object, demonstrate FIFO behavior,")
        # print("      test dequeuing from an empty queue,")
        # print("      test viewing the front of an empty queue,")
        # print("      and verify a single-item queue becomes empty after removal.")

    print("\n\n=== QUEUE DEMO: Ready for Take-Off ===")
    # Group 1, Group 2, Group 3, Group 4

    # Creating the Queue object flight_boarding to represent the queue for boarding a plane
    # This demonstrates FIFO behavior, since the first group to queue is the first group to board (first in, first out)
    flight_boarding = Queue()

    # Print statements for commentary
    print("\nThis demo uses the concept of boarding a plane to demonstrate FIFO behavior.")
    print("\nThe first group to queue in line for boarding is the first group allowed on the plane.")
    print("\nThe following four groups are called to queue in designated lanes: ")

    # Adding the four boarding groups to the queue
    flight_boarding.enqueue("Group 1")
    flight_boarding.enqueue("Group 2")
    flight_boarding.enqueue("Group 3")
    flight_boarding.enqueue("Group 4")

    # Printing the current queue contents
    print(f"    {'\n    '.join(flight_boarding.queue_items)}")

    # dequeue-ing to demonstrate FIFO behavior
    print("\nThe desk agent then calls the first two groups to board: ")
    while len(flight_boarding.queue_items) > 2:
        print("    " + flight_boarding.dequeue())

    # mid-dequeue break to check which item is at the front of the queue
    # demonstrates that front() returns the first item in the queue without removing it
    print("\nA grouchy passenger distracts the desk agent, and she loses track of boarding. \nShe looks at her notes to see which group is at the front of the queue.")
    print("Ah yes! " + flight_boarding.front() + ". The desk agent resumes boarding the remaining groups: ")
    while not flight_boarding.is_empty():
        print("    " + flight_boarding.dequeue())

    # Demonstrating what happens when you use dequeue() and front() on an empty queue
    print("\nWhen there are no items in the queue, dequeue() returns: " + flight_boarding.dequeue())
    print("\nWhen there are no items in the queue, front() returns: " + flight_boarding.front())

    # Create a queue with only one item, remove it, and verify the queue is empty afterward.
    # str(len(sample_queue.queue_items)) used to dynamically fill the number of items in the queue after the enqueue/dequeue operations
    sample_queue = Queue()    # initiating the sample queue
    print("\nAs a final example, we've created a new queue. It currently has " + str(len(sample_queue.queue_items)) + " items.")
    sample_queue.enqueue("Backpack")    # enqueue-ing/adding an item
    print("After adding an item, the new queue contains " + str(len(sample_queue.queue_items)) + " item: " + sample_queue.front())
    print("Next, we will remove that item from our queue.")
    sample_queue.dequeue()     # dequeue-ing/removing the item
    print("Now, our queue contains " + str(len(sample_queue.queue_items)) + " items once again.")


if __name__ == "__main__":
    main()
