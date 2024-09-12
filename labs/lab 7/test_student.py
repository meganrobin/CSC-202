
import unittest
import random
from lab7 import LinkedListQueue, sort_linked_list_queue_correctly


class TestLinkedListQueue(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedListQueue()

    def test_sort_with_random_order(self): #Ensures sort func function should correctly sort a randomly ordered queue#
        cards = [i for i in range(1, 14)]
        random.shuffle(cards)
        for card in cards:
            self.queue.enqueue(card)
        sorted_queue = sort_linked_list_queue_correctly(self.queue)
        self.assertEqual(sorted_queue.to_list(), list(range(1,14))[::-1])
        
    def test_sort_backwards_order(self): #Ensure sort func correctly sorts a queue that's in the exact reverse order than the order its supposed to be after the func executes#
        cards = [i for i in range(1, 14)]
        for card in cards:
            self.queue.enqueue(card)
        sorted_queue = sort_linked_list_queue_correctly(self.queue)
        self.assertEqual(sorted_queue.to_list(), list(range(1,14))[::-1])
        
    def test_sort_already_correct_order(self): #Ensure sort func correctly sorts a queue that's already in the correct order#
        cards = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for card in cards:
            self.queue.enqueue(card)
        sorted_queue = sort_linked_list_queue_correctly(self.queue)
        self.assertEqual(sorted_queue.to_list(), list(cards))
        
    def test_sort_with_none_value(self): #Ensure sort func raises typeerror when the given queue is None#
        cards = None
        with self.assertRaises(TypeError):
            sort_linked_list_queue_correctly(cards)

    def test_sort_with_not_linked_list_queue1(self): #Ensure sort func raises typeerror when the given queue is a list#
        cards = [1, 3, 13, 2, 4, 6, 5, 7, 8, 9, 11, 10, 12]
        with self.assertRaises(TypeError):
            sort_linked_list_queue_correctly(cards)

    def test_sort_with_not_linked_list_queue2(self): #Ensure sort func raises typeerror when the given queue is a string#
        cards = "a"
        with self.assertRaises(TypeError):
            sort_linked_list_queue_correctly(cards)


if __name__ == '__main__':
    unittest.main()