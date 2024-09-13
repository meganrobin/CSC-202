import unittest
from lab10 import MinHeap, heap_sort

class TestMinHeap(unittest.TestCase):

    def test_heap_initialization(self):
        heap = MinHeap()
        self.assertEqual(len(heap.heap), 0, "Heap should be initialized empty")

    def test_insert_single_element(self):
        heap = MinHeap()
        heap.insert(10)
        self.assertEqual(heap.peek(), 10, "Peek should return the single element inserted")

    def test_insert_multiple_elements(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(15)
        self.assertEqual(heap.peek(), 5, "Peek should return the minimum element")

    def test_extract_min_single_element(self):
        heap = MinHeap()
        heap.insert(10)
        min_element = heap.extract_min()
        self.assertEqual(min_element, 10, "Extracted element should be the only element in the heap")

    def test_extract_min_multiple_elements(self):
        heap = MinHeap()
        heap.insert(20)
        heap.insert(10)
        heap.insert(15)
        min_element = heap.extract_min()
        self.assertEqual(min_element, 10, "Extracted element should be the minimum element")

    def test_heap_property_after_extract(self):
        heap = MinHeap()
        heap.insert(20)
        heap.insert(10)
        heap.insert(15)
        heap.extract_min()
        self.assertEqual(heap.peek(), 15, "Peek should return the new minimum after extraction")

    def test_insert_after_extract(self):
        heap = MinHeap()
        heap.insert(20)
        heap.insert(10)
        heap.extract_min()
        heap.insert(5)
        self.assertEqual(heap.peek(), 5, "Peek should return the new inserted minimum")

    def test_extract_min_elements_with_same_value(self):
        heap = MinHeap()
        heap.insert(20)
        heap.insert(20)
        heap.insert(20)
        min_element = heap.extract_min()
        self.assertEqual(min_element, 20, "Extracted element should be the minimum element")

    def test_insert_after_extract_elements_with_same_value(self):
        heap = MinHeap()
        heap.insert(20)
        heap.insert(20)
        heap.extract_min()
        heap.insert(40)
        self.assertEqual(heap.peek(), 20, "Peek should return the new inserted minimum")




    def test_heap_sort_basic(self):
        unsorted_list = [5, 3, 8, 4, 2, 9, 1, 7, 6]
        sorted_list = heap_sort(unsorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5, 6, 7, 8, 9], "List should be sorted in ascending order")

    def test_heap_sort_with_repeating_elements(self):
        unsorted_list = [4, 1, 3, 2, 1, 5, 4]
        sorted_list = heap_sort(unsorted_list)
        self.assertEqual(sorted_list, [1, 1, 2, 3, 4, 4, 5], "List should be sorted in ascending order, including handling repeating elements")
    
    def test_heap_sort_with_one_element(self):
        unsorted_list = [1]
        sorted_list = heap_sort(unsorted_list)
        self.assertEqual(sorted_list, [1], "List should just contain the one element passed into it")

    def test_heap_sort_with_all_same_elements(self):
        unsorted_list = [4, 4, 4, 4, 4, 4, 4, 4, 4]
        sorted_list = heap_sort(unsorted_list)
        self.assertEqual(sorted_list, [4, 4, 4, 4, 4, 4, 4, 4, 4], "List should contain 9 4's")

    def test_heap_sort_basic2(self):
        unsorted_list = [50, 30, 80, 40, 20, 90, 10, 70, 60]
        sorted_list = heap_sort(unsorted_list)
        self.assertEqual(sorted_list, [10, 20, 30, 40, 50, 60, 70, 80, 90], "List should be sorted in ascending order")

    def test_heap_sort_not_list(self):
        unsorted_list = "hooray!"
        with self.assertRaises(TypeError):
            heap_sort(unsorted_list)






if __name__ == '__main__':
    unittest.main()
