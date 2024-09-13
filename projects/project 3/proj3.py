class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Add a comparison method for nodes
    def __lt__(self, other):
        # Primary comparison based on frequency
        if self.freq == other.freq:
            # Secondary comparison based on alphabetical order of character
            return self.char < other.char
        return self.freq < other.freq
    
    def __str__(self):
        # String representation of the Node
        return f"Node: {self.char}, Freq: {self.freq}"

class MinHeap:
    def __init__(self):
        self.heap = []

    def enqueue(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0
    
    def __str__(self):
        return '\n'.join(str(node) for node in self.heap)




#Tasks below. 
        
def count_frequency(s):
    #Generate a dictionary that will be key: value pairs of
    # char:frequency
    #return the dictionary
    dictionary = {} #Initialize empty dictionary#
    for char in s:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    return dictionary

def create_priority_queue(frequency):
    """
    Accepts a frequency dictionary and returns a priority queue filled with nodes.
    """
    #Given a dictionary of char:frequency pairs
    #iterate and enqueue onto the priority queue
    #return priority queue
    queue = MinHeap()
    for k in frequency:
        new_node = Node(k, frequency[k])
        queue.enqueue(new_node)
    
    print(str(queue))
    return queue

def build_tree_from_queue(priority_queue):
    """
    Takes a priority queue and constructs the Huffman tree.
    """
    #While priority queue is not empty
    #iteratively build the huffman tree by dequeing 2 nodes
    #left is the first dequeue
    #right is the second dequeue
    #   #   #if you dequeue and queue becomes empty, return left since that is the root
    #Create new node by merging left and right
    #char is the alphabetically first char between left and right
    #add the frequerncies
    #enque that new node
    while priority_queue.is_empty() == False: #While priority queue is not empty
        print("priority queue not empty")

        left = priority_queue.dequeue()
        print("Left node: " + str(left))
        if priority_queue.is_empty(): #if you dequeue and queue becomes empty, return left since that is the root
            print("priority queue is empty")
            return left
        
        right = priority_queue.dequeue()
        print("Right node: " + str(right))
        
        new_node = Node(left.char, (left.freq + right.freq))
        new_node.left = left
        new_node.right = right
        priority_queue.enqueue(new_node)

    return priority_queue.dequeue()


def generate_codes(node, prefix="", code=None):
    if code is None:
        code = {}

    #Traverse the tree to generate a huffman encoding
    # the huffman encoding will be a dictionary char:encoding pairs
    #if node is Node return None
    #if node has a char, then code[node.char] = prefix
    #recursively calls generate_codes on the left, with prefix + "0" and code
    #recursively calls generate_codes on the right, with prefix + "1" and code
    #returns the code dictionary
    
    if node is None:
        return None
    
    if node.char is not None:
        code[node.char] = prefix
    
    if node.left is not None:
        generate_codes(node.left, prefix + "0", code)
    if node.right is not None:
        generate_codes(node.right, prefix + "1", code)

    return code

def encode(s, codes):
    #This is given to you
    return ''.join(codes[char] for char in s)

def decode(encoded_string, root):
    #for decode accept the encoded string, and the root of the huffman tree and producce a decoded string
    #go char by char in the encoded string, each char representing a bit
    #you'll need to travese your tree
    #if the bit is 0 go left,
    #if the bit is 1 go right
    # continue until you reach a leaf node and concatinate that char to your decoded string
    #return the new string
    new_string = ""
    leaf = root
    for character in encoded_string:
        if character == "0":
            leaf = leaf.left
        elif character == "1":
            leaf = leaf.right
        
        if leaf.left is None and leaf.right is None:
            new_string += leaf.char
            leaf = root

    return new_string


def huffman_encoding(s):
    #This will be your main function
    #get the freq dictionary for the string
    freq_dictionary = count_frequency(s)
    #get the priority queue from the freq dictionary
    priority_queue = create_priority_queue(freq_dictionary)
    #get the root of your huffman tree given the pq
    tree_root = build_tree_from_queue(priority_queue)
    print(tree_root)
    print(tree_root.left.left)
    #get your encodings dictionary from searching your tree
    code_dictionary = generate_codes(tree_root)
    for i in code_dictionary:
        print(i)
        print(code_dictionary[i])
    #get your encoding string
    encoded_string = encode(s, code_dictionary)
    #decode your string
    decoded_string = decode(encoded_string, tree_root)
    #return your encoded string, decoded string, and encoding dictionary
    
    return [encoded_string, decoded_string, code_dictionary]


print(huffman_encoding("hello"))
