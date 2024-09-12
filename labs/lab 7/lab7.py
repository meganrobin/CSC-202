"""Task1: Complete the implementation details for enqueue and dequeue"""

class Node:
    """A Node in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    """A Queue implementation using a linked list."""
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, value):
        """Add an item to the rear of the queue."""
        new_node = Node(value)
        if self.rear is not None:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        """Remove an item from the front of the queue."""
        if self.is_empty(): #Returns None if the queue is empty#
            return None

        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        """Peek at the front item of the queue without removing it."""
        if self.is_empty():
            return None
        return self.front.value

    def to_list(self):
        """Convert the queue to a list for easy viewing."""
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return elements[::-1]


"""Task 2: Write test cases for the solution queue function in Task 3 in test_student.py, and doc string for the function"""


"""Task 3: Complete the get solution queue where the result is a solution queue that goes from high to low"""


def sort_linked_list_queue_correctly(queue):
    """
    Sorts a linked list queue from high to low using the specified method.
    
    Args:
    queue (LinkedListQueue): A linked list queue to be sorted.

    Returns:
    LinkedListQueue: A new sorted queue.
    """
    if not isinstance(queue, LinkedListQueue):
        raise TypeError

    sorted_queue = LinkedListQueue()
    counter = 1
    while not queue.is_empty(): #While the original queue isn't empty#
        t = queue.peek_front() #t is the value of the first node enqueued to original queue#
        queue.dequeue()
        if t == counter:
            sorted_queue.enqueue(t)
            counter += 1
        else:
            queue.enqueue(t)
    
    return sorted_queue

# Create a linked list queue and add elements
#use this for debugging purposes

import random
queue = LinkedListQueue()
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(cards)
print(cards)
for card in cards:
    queue.enqueue(card)

# Sort the queue using the corrected method
sorted_queue_correctly = sort_linked_list_queue_correctly(queue)
print(sorted_queue_correctly.to_list()) # Convert the sorted queue to a list for display






"""Task4: No Submission for this task. What is the time complexity of your solution?"""
#I think the time complexity of my solution is O(n)#


