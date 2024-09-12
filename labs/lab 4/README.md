# Lab 4: Singly Linked List Operations

## Overview
Lab 4 focuses on implementing and manipulating singly linked lists in Python. You will work on three primary tasks, each designed to enhance your understanding of linked lists and their applications.

### Task 1: Implement `append` Method
Your first task is to complete the `append` method in the `LinkedList` class. This method should add a new node with the given data to the end of the list. It's important to note that you should accomplish this without using a tail pointer.

**Guidelines:**
- Traverse the list starting from the head.
- Add the new node when you reach the end of the list.

### Task 2: Combine Two Linked Lists
The second task involves writing a function, `combine_linked_lists`, that takes two `LinkedList` instances and combines them into one list.

**Key Points:**
- Ensure both arguments are instances of `LinkedList`.
- Handle cases where either list is `None` or empty.
- Attach the end of the first list to the beginning of the second list.

### Task 3: Check if a Linked List is a Palindrome
The final task is to complete the `is_palindrome` function. This function should determine whether a given linked list is a palindrome.

**Procedure:**
- Check if the input list is `None` or empty.
- Convert the linked list to a Python list for easier comparison.
- Determine if the list is the same forwards and backwards.

## Submission Guidelines
Please ensure your code adheres to the provided specifications for each task. After completing the tasks, submit your Python scripts via github commit&sync

