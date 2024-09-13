import unittest
from proj1 import LinkedList, Calculator

class TestPolynomialAntiDerivativeEdgeCases(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def create_linked_list(self, coefficients):
        ll = LinkedList()
        for coeff in coefficients:
            ll.append(coeff)
        return ll
    
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    #Leave the above methods alone

    def test_example(self):
        poly1 = self.create_linked_list([1, 2, 3])
        poly2 = self.create_linked_list([4, 5, 6])
        result = self.calc.add_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [5, 7, 9])

    def test_add_simple_polynomials(self):
        poly1 = self.create_linked_list([1, 2, 3])
        poly2 = self.create_linked_list([4, 5, 6])
        result = self.calc.add_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [5, 7, 9])

    def test_add_different_length_polynomials(self):
        poly1 = self.create_linked_list([2, 0, 40])
        poly2 = self.create_linked_list([50, 60])
        result = self.calc.add_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [2, 50, 100])

    def test_add_polynomials_with_negatives(self):
        poly1 = self.create_linked_list([-1, -2, -3])
        poly2 = self.create_linked_list([1, -2, -3])
        result = self.calc.add_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [0, -4, -6])

    def test_add_polynomials_resulting_in_higher_degree(self):
        poly1 = self.create_linked_list([3, 40])
        poly2 = self.create_linked_list([1, 2, 3])
        result = self.calc.add_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [1, 5, 43])

    def test_subtract_same_polynomials(self):
        poly1 = self.create_linked_list([1, 65, 67, 8])
        poly2 = self.create_linked_list([1, 65, 67, 8])
        result = self.calc.subtract_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [0, 0, 0, 0])

    def test_subtract_polynomials_negative_coefficients(self):
        poly1 = self.create_linked_list([-1, -2, -10])
        poly2 = self.create_linked_list([1, 2, 10])
        result = self.calc.subtract_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [-2, -4, -20])

    def test_subtract_polynomials_large_coefficients(self):
        poly1 = self.create_linked_list([100, 200, 300])
        poly2 = self.create_linked_list([10, 20, 30])
        result = self.calc.subtract_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [90, 180, 270])

    def test_subtract_polynomials_mixed_coefficients(self):
        poly1 = self.create_linked_list([-3, -2, -5])
        poly2 = self.create_linked_list([6, -7, 8])
        result = self.calc.subtract_polynomials(poly1.head, poly2.head)
        self.assertEqual(self.linked_list_to_list(result), [-9, 5, -13])

    def test_differentiate_higher_degree_polynomial(self):
        poly = self.create_linked_list([3, 0, 7, 2])
        result = self.calc.differentiate_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [9, 0, 7])

    def test_differentiate_polynomial_negatives(self):
        poly = self.create_linked_list([-5, -1, -80])
        result = self.calc.differentiate_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [-10, -1])

    def test_differentiate_polynomial_single_term(self):
        poly = self.create_linked_list([1])
        result = self.calc.differentiate_polynomial(poly.head)
        self.assertIsNone(result)
    
    def test_differentiate_polynomial_with_zero_and_non_zero_coefficients(self):
        poly = self.create_linked_list([0, 0, 4, 0, 7])
        result = self.calc.differentiate_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [0, 0, 8, 0])

    def test_anti_derivative_simple_polynomial(self):
        poly = self.create_linked_list([4, 3, 6])
        result = self.calc.anti_derivative_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [4/3, 3/2, 6, 0])

    def test_anti_derivative_polynomial_negative_coefficients(self):
        poly = self.create_linked_list([-3, -2, -1])
        result = self.calc.anti_derivative_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [-1.0, -1.0, -1.0, 0])

    def test_anti_derivative_polynomial_large_coefficients(self):
        poly = self.create_linked_list([10, 20000, 300])
        result = self.calc.anti_derivative_polynomial(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [10/3, 10000.0, 300.0, 0])

    def test_anti_derivative_single_negative_term(self):
        poly = self.create_linked_list([-5])
        result = self.calc.anti_derivative_polynomial(poly.head)
        self.assertIsNotNone(result)

    def test_anti_derivative_single_zero_term(self):
        poly = self.create_linked_list([0])
        result = self.calc.anti_derivative_polynomial(poly.head)
        self.assertIsNotNone(result)

    def test_reverse_simple_polynomial(self):
        poly = self.create_linked_list([1, 2, 3])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [3, 2, 1])

    def test_reverse_polynomial_with_negatives(self):
        poly = self.create_linked_list([-11, -2, -3])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [-3, -2, -11])

    def test_reverse_empty_polynomial(self):
        poly = self.create_linked_list([])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [])

    def test_reverse_zero_and_non_zero_coefficients(self):
        poly = self.create_linked_list([0, 0, 4, 0, 7])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [7, 0, 4, 0, 0])

    def test_reverse_single_term(self):
        poly = self.create_linked_list([3])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [3])

    def test_reverse_single_zero_term(self):
        poly = self.create_linked_list([0])
        result = self.calc.reverse(poly.head)
        self.assertEqual(self.linked_list_to_list(result), [0])

if __name__ == '__main__':
    unittest.main()
