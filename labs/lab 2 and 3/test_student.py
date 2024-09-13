import unittest
from lab2 import max_list_iter, reverse_rec, bin_search

class TestLab2(unittest.TestCase):

    # Tests for max_list_iter
    def test_max_list_iter_custom1(self):
        # Add your custom test case here
        self.assertEqual(max_list_iter([-3,]), -3)

    def test_max_list_iter_custom2(self):
        # Add your custom test case here
        self.assertEqual(max_list_iter([-3, 5, 0, 5, 7, 5, 5, 5]), 7)

    # Tests for reverse_rec
    def test_reverse_rec_custom1(self):
        self.assertEqual(reverse_rec([-4]), [-4])

    def test_reverse_rec_custom2(self):
        self.assertEqual(reverse_rec([100, 300]), [300, 100])

    # Tests for bin_search
    def test_bin_search_custom1(self):
        self.assertIsNone(bin_search(3, 0, 3, [1, 7, 7, 7]))

    def test_bin_search_custom2(self):
        self.assertIsNone(bin_search(3, 3, 0, [1, 7, 7, 7]))

if __name__ == '__main__':
    unittest.main()
