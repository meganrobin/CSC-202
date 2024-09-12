import unittest
from lab5 import reverse_stack, process_card_stack, ArrayStack
import random

class TestStudent(unittest.TestCase):
    def setUp(self):
        #Common setup for each test case
        self.capacity = 13

    def test_push_pop(self):
        #Test pushing
        self.stack1 = ArrayStack(self.capacity)
        test_items = [0, 1, 2, 3]
        for item in test_items:
            self.stack1.push(item)
        #Test popping
        for item in reversed(test_items):
            self.assertEqual(self.stack1.pop(), item)
        
        #Test pushing
        self.stack2 = ArrayStack(self.capacity)
        test_items = [30, 70, 500, 50, 1, 5, 6, 7, 8]
        for item in test_items:
            self.stack2.push(item)
        #Test popping
        for item in reversed(test_items):
            self.assertEqual(self.stack2.pop(), item)

    def test_push_pop_empty_stack(self):
        #Test pushing into a full stack
        self.stack = ArrayStack(self.capacity)
        for i in range(self.capacity):
            self.stack.push(i)

        with self.assertRaises(Exception) as context:
            self.stack.push(6)
        self.assertTrue('Stack is full' in str(context.exception))
    
    def test_push_full_stack(self):
        #Test pushing into a full stack
        self.stack = ArrayStack(self.capacity)
        for i in range(self.capacity):
            self.stack.push(i)

        with self.assertRaises(Exception) as context:
            self.stack.push(6)
        self.assertTrue('Stack is full' in str(context.exception))
    
    def test_reverse(self):
        #Test with a non-empty stack
        stack = ArrayStack(13)
        for item in [2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7]:
            stack.push(item)

        reversed_stack = reverse_stack(stack)
        reversed_items = [reversed_stack.pop() for _ in range(reversed_stack.size())]
        self.assertEqual(reversed_items, [2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 4, 6, 7])

    def test_reverse_full_capacity(self):
        #Test with a stack at full capacity
        stack = ArrayStack(3)
        for item in [1, 2, 3]:
            stack.push(item)

        reversed_stack = reverse_stack(stack)
        reversed_items = [reversed_stack.pop() for _ in range(reversed_stack.size())]
        self.assertEqual(reversed_items, [1, 2, 3])

    def test_sort_normal(self):
        #Test with cards in a random order
        cardStack = ArrayStack(self.capacity)
        list = [3, 6, 4, 1, 2, 5, 9, 8, 7, 10, 13, 12, 11]
        random.shuffle(list)
        for card in list:
            cardStack.push(card)

        result = process_card_stack(cardStack)
        expected_solution = [i for i in range(1,14)]
        actual_solution = [result.pop() for _ in range(result.size())]
        self.assertEqual(actual_solution, expected_solution[::-1])

    def test_sort_not_stack(self):
        #Test with input that is not a stack
        non_stack_input = ["A", "B", "C"]
        with self.assertRaises(TypeError):
            process_card_stack(non_stack_input)
    
if __name__ == '__main__':
    unittest.main()