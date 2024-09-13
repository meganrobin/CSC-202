class LinkedListQueue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item):
        newNode = self.Node(item)
        if self.tail:
            self.tail.next = newNode
        self.tail = newNode
        if not self.head:
            self.head = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

class LinkedListStack:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, item):
        newNode = self.Node(item, self.top)
        self.top = newNode

    def pop(self):
        if self.isEmpty():
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.value


def bottomUpBFS(root):
    """
    Perform a bottom-up level order traversal of a binary tree.

    Args:
    - root: The root of the binary tree.

    Returns:
    - A LinkedListQueue containing the nodes' values in bottom-up level order.
    
    Recommend Steps to follow:
    1. Check if the tree is empty. If so, return an empty LinkedListQueue.
    2. Initialize a LinkedListQueue for BFS traversal and enqueue the root node.
    3. Initialize a LinkedListStack to collect nodes in reverse BFS order.
    4. While the BFS queue is not empty, continue processing:
       a. Dequeue a node from the queue.
       b. Push the node's value onto the result stack. This step reverses the order of traversal.
       c. Enqueue the node's children into the BFS queue. IMPORTANT: To maintain the correct order
          when reversed, enqueue the right child first, then the left child, if they exist.
    5. After the BFS traversal is complete and all nodes are in the stack,
       transfer them to a new LinkedListQueue. This reverses the order, creating the bottom-up result.
    6. Return the queue containing the bottom-up level order traversal of the tree.

    Additional guidance:
    - Pay attention to the order in which children are added to the queue during BFS.
    - Ensure the stack correctly reverses the order of nodes as intended.
    - Carefully transfer nodes from the stack back to a queue to finalize the bottom-up order.
    """
    if root is None:
        return LinkedListQueue()

    ll_queue = LinkedListQueue() #Initialize queue#
    ll_queue.enqueue(root)

    ll_stack = LinkedListStack() #Initialize stack#

    while not ll_queue.isEmpty():
        current_node = ll_queue.dequeue()
        ll_stack.push(current_node.value)
        
        if current_node.right is not None: #Enqueue right child if it exists#
            ll_queue.enqueue(current_node.right)
        if current_node.left is not None: #Enqueue left child if it exists#
            ll_queue.enqueue(current_node.left)

    new_ll_queue = LinkedListQueue() #Initialize new queue to hold the new bottom-up result#
    while not ll_stack.isEmpty():
        new_ll_queue.enqueue(ll_stack.pop())

    return new_ll_queue
