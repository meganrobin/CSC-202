class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sortedListToBST(nums):
    """
    Converts a sorted list of integers into a balanced Binary Search Tree (BST).

    Args:
    - nums (List[int]): A sorted list of integers in ascending order.

    Returns:
    - TreeNode: The root node of the resulting balanced BST.

    Procedure:
    1. Identify the base case for the recursive function. What should be returned if 'nums' is empty?
    2. Determine the middle index of the list. This element will be the root of the current subtree.
    3. Create a new TreeNode with the value of the middle element. 
    4. Recursively call this function to construct the left subtree from the sub-list to the left of the middle element.
    5. Similarly, construct the right subtree from the sub-list to the right of the middle element.
    6. Assign the left and right subtrees to the root node's left and right pointers, respectively.
    7. Return the root node of the subtree.
    """
    if not isinstance(nums, list) or len(nums) == 0: #Returns None if parameter var nums is not a list or if it's an empty list#
        return None

    def Helper(start, end): #Helper recursive function to build out the tree#
        if start > end:
            return None #Returns None if there's no more children to add#
        middle = (start + end)//2 #Calculates the middle TreeNode of the sublist#
        root = TreeNode(nums[middle])
        #Assigns the root's left and right pointers to the left and right subtrees respectively#
        root.left = Helper(start, middle - 1)
        root.right = Helper(middle + 1, end)

        return root
    
    return Helper(0, len(nums) - 1) #Starts the recursion helper function by initially passing 0 as the starting index and original length - 1 as the ending index#


def isValidBST(root, left=float('-inf'), right=float('inf')):
    """
    Determines if a binary tree is a valid Binary Search Tree (BST).

    Args:
    - root (TreeNode): The root node of the binary tree.
    - left (int): The lower bound for the current node's value. Defaults to negative infinity.
    - right (int): The upper bound for the current node's value. Defaults to infinity.

    Returns:
    - bool: True if the binary tree is a valid BST, False otherwise.

    Procedure:
    1. Define the base case for the recursive function. What should be returned if 'root' is None?
    2. Check if the current node's value is within the valid range (greater than 'left' and less than 'right').
    3. Recursively validate the left subtree, updating the upper bound to the current node's value.
    4. Recursively validate the right subtree, updating the lower bound to the current node's value.
    5. If both the left and right subtrees are valid, return True. Otherwise, return False.
    """
    if not isinstance(root, TreeNode) or root == None: #Returns None if parameter var root is not a TreeNode#
        return False

    def solve(root, left, right):
            if root is None:
                return True
            
            if root.value <= left or root.value >= right:
                return False

            l = solve(root.left, left, root.value)
            r = solve(root.right, root.value, right)
            return l and r

    return solve(root, float('-inf'), float('inf'))

def areSameTree(p, q):
    """
    Checks if two binary trees are the same.

    Args:
    - p (TreeNode): The root node of the first binary tree.
    - q (TreeNode): The root node of the second binary tree.

    Returns:
    - bool: True if the two trees are identical, False otherwise.

    Procedure:
    1. Check if both trees are empty. If so, they are identical.
    2. If one tree is empty and the other is not, or if the current nodes' values don't match, the trees are not identical.
    3. Recursively check if the left subtrees are identical.
    4. Recursively check if the right subtrees are identical.
    5. If both the left and right subtrees are identical, return True. Otherwise, return False.
    """
    #Returns True if they're both empty, because these are the last children in the tree
    if p == None and q == None:
        return True
 
    #Compares the node values if both nodes are not empty, recalls areSameTree if they have the same value or returns False if they have different values in the same spot
    if p != None and q != None:
        return ((p.value == q.value) and areSameTree(p.left, q.left) and areSameTree(p.right, q.right))
 
    #Return False if one is empty and the other is not
    return False
