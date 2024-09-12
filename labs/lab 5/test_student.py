import unittest
from lab5 import DoublyLinkedList

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
        for i in range(1, 10): #1, 2, 3, 4, 5, 6, 7, 8, 9, 10#
            self.dll.append(i)
    
    def test_eq_same(self):
        other_dll = DoublyLinkedList()
        for i in range(1, 10):
            other_dll.append(i)
        self.assertTrue(self.dll == other_dll)
    
    def test_eq_different(self):
        other_dll = DoublyLinkedList()
        for i in range(4, 7):
            other_dll.append(i)
        self.assertFalse(self.dll == other_dll)
    
    def test_get_item_1(self):
        self.assertEqual(self.dll[3], 4)
    
    def test_get_item_2(self):
        self.assertEqual(self.dll[5], 6)
    
    def test_get_index_out_of_range(self):
        with self.assertRaises(IndexError):
            _ = self.dll[14]
    def test_set_item_1(self):
        self.dll[0] = 2
        self.assertEqual(self.dll[0], 2)

    def test_set_item_2(self):
        self.dll[7] = 0
        self.assertEqual(self.dll[7], 0)

    def test_set_item_3(self):
        self.dll[3] = 6
        self.assertEqual(self.dll[3], 6)

    def test_set_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.dll[30] = 100



if __name__ == '__main__':
    unittest.main()
