import unittest
from proj3 import Node, MinHeap, count_frequency, create_priority_queue, build_tree_from_queue, generate_codes, encode, decode, huffman_encoding

class TestHuffmanEncoding(unittest.TestCase):
    def test_count_frequency_chirp(self):
        input_string = "chirp"
        expected_dictionary = {'c': 1, 'h': 1, 'i': 1, 'r': 1, 'p': 1}
        self.assertEqual(count_frequency(input_string), expected_dictionary)
        
    def test_count_frequency_coffee(self):
        input_string = "coffee"
        expected_dictionary = {'c': 1, 'o': 1, 'f': 2, 'e': 2}
        self.assertEqual(count_frequency(input_string), expected_dictionary)
    

    def test_create_priority_queue_chirp(self):
        dictionary = {'c': 1, 'h': 1, 'i': 1, 'r': 1, 'p': 1}
        priority_queue = create_priority_queue(dictionary)
        expected_queue = MinHeap()
        expected_queue.heap = [Node('c', 1), Node('h', 1), Node('i', 1), Node('r', 1), Node('p', 1)]
        for i in range(5):
            self.assertEqual((priority_queue.heap[i]).char, (expected_queue.heap[i]).char)
            self.assertEqual((priority_queue.heap[i]).freq, (expected_queue.heap[i]).freq)

    def test_create_priority_queue_coffee(self):
        dictionary = {'c': 1, 'o': 1, 'f': 2, 'e': 2}
        priority_queue = create_priority_queue(dictionary)
        expected_queue = MinHeap()
        expected_queue.heap = [Node('c', 1), Node('o', 1), Node('f', 2), Node('e', 2)]
        for i in range(4):
            self.assertEqual((priority_queue.heap[i]).char, (expected_queue.heap[i]).char)
            self.assertEqual((priority_queue.heap[i]).freq, (expected_queue.heap[i]).freq)

    def test_build_tree_from_queue_chirp(self):
        dictionary = {'c': 1, 'h': 1, 'i': 1, 'r': 1, 'p': 1}
        priority_queue = create_priority_queue(dictionary)
        tree_root = build_tree_from_queue(priority_queue)

        self.assertEqual(tree_root.char, "i")
        self.assertEqual(tree_root.freq, 5)
        self.assertEqual(tree_root.left.char, "i")
        self.assertEqual(tree_root.left.freq, 2)
        self.assertEqual(tree_root.right.char, "r")
        self.assertEqual(tree_root.right.freq, 3)
        self.assertEqual(tree_root.left.left.char, "i")
        self.assertEqual(tree_root.left.left.freq, 1)
        self.assertEqual(tree_root.left.right.char, "p")
        self.assertEqual(tree_root.left.right.freq, 1)
        self.assertEqual(tree_root.right.left.char, "r")
        self.assertEqual(tree_root.right.left.freq, 1)
        self.assertEqual(tree_root.right.right.char, "c")
        self.assertEqual(tree_root.right.right.freq, 2)
        self.assertEqual(tree_root.right.right.left.char, "c")
        self.assertEqual(tree_root.right.right.left.freq, 1)
        self.assertEqual(tree_root.right.right.right.char, "h")
        self.assertEqual(tree_root.right.right.right.freq, 1)
        self.assertEqual(tree_root.right.right.right.right, None)
        self.assertEqual(tree_root.right.right.right.left, None)
        
    def test_build_tree_from_queue_coffee(self):
        dictionary = {'c': 1, 'o': 1, 'f': 2, 'e': 2}
        priority_queue = create_priority_queue(dictionary)
        tree_root = build_tree_from_queue(priority_queue)

        self.assertEqual(tree_root.char, "f")
        self.assertEqual(tree_root.freq, 6)
        self.assertEqual(tree_root.left.char, "f")
        self.assertEqual(tree_root.left.freq, 2)
        self.assertEqual(tree_root.right.char, "c")
        self.assertEqual(tree_root.right.freq, 4)
        self.assertEqual(tree_root.left.left, None)
        self.assertEqual(tree_root.left.right, None)
        self.assertEqual(tree_root.right.left.char, "c")
        self.assertEqual(tree_root.right.left.freq, 2)
        self.assertEqual(tree_root.right.left.left.char, "c")
        self.assertEqual(tree_root.right.left.left.freq, 1)
        self.assertEqual(tree_root.right.left.right.char, "o")
        self.assertEqual(tree_root.right.left.right.freq, 1)
        self.assertEqual(tree_root.right.right.char, "e")
        self.assertEqual(tree_root.right.right.freq, 2)
        self.assertEqual(tree_root.right.right.left, None)
        self.assertEqual(tree_root.right.right.right, None)

    def test_generate_codes_chirp(self):
        priority_queue = create_priority_queue({'c': 1, 'h': 1, 'i': 1, 'r': 1, 'p': 1})
        tree_root = build_tree_from_queue(priority_queue)
        expected_codes = {'i': '00', 'p': '01', 'r': '10', 'c': '110', 'h': '111'}
        self.assertEqual(generate_codes(tree_root), expected_codes)

    def test_generate_codes_bamboo(self):
        priority_queue = create_priority_queue({'b': 2, 'a': 1, 'm': 1, 'o': 2})
        tree_root = build_tree_from_queue(priority_queue)
        expected_codes = {'o': '0', 'b': '11', 'a': '100', 'm': '101'}
        self.assertEqual(generate_codes(tree_root), expected_codes)

    def test_encode_chirp(self):
        codes = {'i': '00', 'p': '01', 'r': '10', 'c': '110', 'h': '111'}
        self.assertEqual(encode("chirp", codes), "110111001001")

    def test_encode_bamboo(self):
        codes = {'o': '0', 'b': '11', 'a': '100', 'm': '101'}
        self.assertEqual(encode("bamboo", codes), "111001011100")

    def test_decode_chirp(self):
        priority_queue = create_priority_queue({'c': 1, 'h': 1, 'i': 1, 'r': 1, 'p': 1})
        tree_root = build_tree_from_queue(priority_queue)
        codes = {'i': '00', 'p': '01', 'r': '10', 'c': '110', 'h': '111'}
        self.assertEqual(decode("110111001001", tree_root), "chirp")

    def test_decode_bamboo(self):
        priority_queue = create_priority_queue({'b': 2, 'a': 1, 'm': 1, 'o': 2})
        tree_root = build_tree_from_queue(priority_queue)
        codes = {'o': '0', 'b': '11', 'a': '100', 'm': '101'}
        self.assertEqual(decode("111001011100", tree_root), "bamboo")

    def test_huffman_encoding_clipping(self):
        input_string = "clipping"
        expected_encoded = "00010001111101101001"
        expected_codes = {'i': '01', 'p': '11', 'c': '000', 'g': '001', 'l': '100', 'n': '101'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_huffman_encoding_bamboo(self):
        input_string = "bamboo"
        expected_encoded = "111001011100"
        expected_codes = {'o': '0', 'b': '11', 'a': '100', 'm': '101'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

if __name__ == "__main__":
    unittest.main()