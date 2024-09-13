import unittest
from proj2 import bottomUpBFS, LinkedListQueue  # Ensure LinkedListQueue is accessible for the test

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def queueToList(queue):
    """Convert a LinkedListQueue to a list."""
    result = []
    while not queue.isEmpty():
        result.append(queue.dequeue())
    return result


class TestBottomUpBFS(unittest.TestCase):
    def test_complicated_tree(self):
        """Test a more complicated tree structure"""
        root = TreeNode(3, TreeNode(1, None, TreeNode(8, TreeNode(4), TreeNode(7))), TreeNode(2, TreeNode(11), TreeNode(5, TreeNode(10), TreeNode(12))))
        expected = [4, 7, 10, 12, 8, 11, 5, 1, 2, 3]
        self.assertEqual(queueToList(bottomUpBFS(root)), expected)

    def test_same_values_tree(self):
        """Test a tree with multiple of the same value"""
        root = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1, TreeNode(1))))
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(queueToList(bottomUpBFS(root)), expected)

    def test_super_right_skewed_tree(self):
        """Test a tree with all right children (excluding root node)"""
        root = TreeNode(1, None, TreeNode(4, None, TreeNode(3, None, TreeNode(6, None, TreeNode(7)))))
        expected = [7, 6, 3, 4, 1]
        self.assertEqual(queueToList(bottomUpBFS(root)), expected)

    def test_super_left_skewed_tree(self):
        """Test a tree with all right children (excluding root node)"""
        root = TreeNode(1, TreeNode(4, TreeNode(3, TreeNode(6, TreeNode(7)))))
        expected = [7, 6, 3, 4, 1]
        self.assertEqual(queueToList(bottomUpBFS(root)), expected)




if __name__ == "__main__":
    unittest.main()