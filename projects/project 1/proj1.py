class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)

class Calculator:

    def reverse(self, current):
        """Input: the head node of a singly linked lists representing a polynomial
            Operation: reverses the polynomial term by term
            Output: the head node of a new singly linked list that represents the reversed polynomial"""
        
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        poly1 = previous

        return poly1
        
    def add_polynomials(self, poly1, poly2): #Params are the head of each polynomial (which is linked to the rest of the polynomial through the linked list next system)#
        """Input: the head nodes of two singly linked lists representing polynomials
            Operation: adds the polynomials term by term, appropriately handles cases when polynomials are of different lengths
            Output: the head node of a new singly linked list that represents the two polynomials added together"""
        
        #Typeerror checks
        if (isinstance(poly1, list)) or (isinstance(poly2, list)): #Makes sure input isn't a list#
            raise TypeError
            
        if poly1 is None or poly2 is None: #Makes sure input isn't none#
            raise TypeError

        #Reverse inputs
        current1 = self.reverse(poly1)
        current2 = self.reverse(poly2)
        current3 = Node()
        head = current3

        while current1 or current2:
            if current1 is None: #If the first polynomial doesn't have a term in this position, just takes the term from the second polynomial for this position#
                if current2.val != 0: #Ensures that the first polynomial's term is not 0#
                    current3.next = Node(current2.val)
                if current2.next: #If 2nd polynomial has more values in the ll#
                    current2 = current2.next
                else: #If 2nd polynomial doesn't have anymore values in the ll#
                    current2 = None #Sets 2nd polynomial to none to stop the while loop from iterating again#
                current3 = current3.next

            elif current2 is None:
                current3.next = Node(current1.val)
                if current1.next: #If 1st polynomial has more values in the ll#
                    current1 = current1.next
                else: #If 1st polynomial doesn't have anymore values in the ll#
                    current1 = None #Sets 1st polynomial to none to stop the while loop from iterating again#
                current3 = current3.next

            else: #Add straight on
                current3.next = Node(current1.val + current2.val)
                current1 = current1.next
                current2 = current2.next
                current3 = current3.next


        return self.reverse(head.next)
    
    def subtract_polynomials(self, poly1, poly2):
        """Input: the head nodes of two singly linked lists representing polynomials
            Operation: subtracts the second polynomial from the first polynomial, term by term, appropriately handles cases when polynomials are of different lengths or when the second polynomial has a term with a 0 value
            Output: the head node of a new singly linked list that represents the second polynomial subtracted from the first polynomial"""
        
        #Typeerror checks
        if (isinstance(poly1, list)) or (isinstance(poly2, list)): #Makes sure input isn't a list#
            raise TypeError
            
        if poly1 is None or poly2 is None: #Makes sure input isn't none#
            raise TypeError

        #Reverse inputs
        current1 = self.reverse(poly1)
        current2 = self.reverse(poly2)
        current3 = Node()
        head = current3
        
        while current1 or current2:
            if current1 is None: #If the first polynomial doesn't have a term in this position, just takes the term from the second polynomial for this position#
                if current2.next: #If 2nd polynomial has more values in the ll#
                    current3.next = Node(-1 * current2.val)
                    current2 = current2.next
                else: #If 2nd polynomial doesn't have anymore values in the ll#
                    current3.next = Node(-1 * current2.val)
                    current2 = None #Sets 2nd polynomial to none to stop the while loop from iterating again#
                current3 = current3.next

            elif current2 is None:
                if current1.next: #If 1st polynomial has more values in the ll#
                    current3.next = Node(current1.val)
                    current1 = current1.next
                else: #If 1st polynomial doesn't have anymore values in the ll#
                    current3.next = Node(current1.val)
                    current1 = None #Sets 1st polynomial to none to stop the while loop from iterating again#
                current3 = current3.next

            else: #Subtract straight on
                if current2 == 0:
                    current3.next = Node(current1.val)
                    current1 = current1.next
                    current2 = current2.next
                    current3 = current3.next
                else:
                    current3.next = Node(current1.val - current2.val)
                    current1 = current1.next
                    current2 = current2.next
                    current3 = current3.next


        return self.reverse(head.next)

    def differentiate_polynomial(self, poly):
        """Input: the head node of a singly linked lists representing a polynomial
            Operation: differentiates the polynomial term by term, using a count variable to keep track of the variable's power
            Output: the head node of a new singly linked list that represents the differentiated polynomial"""

        #Typeerror checks
        if isinstance(poly, list) or poly is None or isinstance(poly.val, str): #Makes sure input isn't a list or None or that the first head is a non-numeric value#
            raise TypeError

        #Reverse input
        current = self.reverse(poly)
        current_outcome = Node()
        head = current_outcome

        if current.val == 0: #Catches the error where it's all zero terms#
            if current.next:
                if current.next.val == 0:
                    if current.next.next:
                        if current.next.next.val == 0:
                            return None

        count = 0 #Iterator#
        while current:
            if count == 0: #Doesn't put the first term encountered into the differentiated ll, since it's the last term of the polynomial which gets dropped through differentiation#
                pass
            else:
                current_outcome.next = Node(count * current.val)
                current_outcome = current_outcome.next

            count += 1 #Increase counter with each iteration#
            if current.next: #If the polynomial has more terms to iterate over#
                current = current.next #Makes the next head the current head#
            else:
                current = None

        return self.reverse(head.next)

    def anti_derivative_polynomial(self, poly):
        """Input: the head node of a singly linked lists representing a polynomial
            Operation: computes the anti-derivative of the polynomial term by term, using a count variable to keep track of the variable's power
            Output: the head node of a new singly linked list that represents the anti-differentiated polynomial"""
        #Typeerror checks
        if isinstance(poly, list) or poly is None or isinstance(poly.val, str): #Makes sure input isn't a list or None or that the first head is a non-numeric value#
            raise TypeError

        #Reverse input
        current = self.reverse(poly)
        current_outcome = Node()
        head = current_outcome

        count = 0 #Iterator#
        while current:
            if count == 0: #Ensures that the last term of the result ll is 0#
                current_outcome.next = Node(0)
                current_outcome = current_outcome.next
                count += 1 #Increase counter with each iteration#
            else:
                current_outcome.next = Node(current.val / count)
                current_outcome = current_outcome.next
                count += 1 #Increase counter with each iteration#
                if current.next: #If the polynomial has more terms to iterate over#
                    current = current.next #Makes the next head the current head#
                else:
                    current = None

            
        
        return self.reverse(head.next)
    
