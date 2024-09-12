"""Task1: complete the append method WITHOUT using a tail"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)


"""Task2: Give two lists combine them into one list"""
def combine_linked_lists(list1, list2):
    # Check if both arguments are LinkedList instances
    if isinstance(list1, LinkedList) and isinstance(list2, LinkedList):
        pass
    else:
        raise TypeError

    # Check if any of the lists is None
    if list1 == None or list2 == None:
        return None
    
    # If the first list is empty, return the second list
    if  list1.head == None:
        return list2

    # If the second list is empty, return the first list
    if  list2.head == None:
        return list1

    # Find the end of the first list
    last = list1.head
    while last.next:
        last = last.next

    # Link the end of the first list to the start of the second list
    
    last.next = list2.head

    #return the new list
    return list1

"""Task3: Complete the function to determine is a linked list is a palindrome """
def is_palindrome(llist):
    # Check if the linked list is None or empty
    if isinstance(llist, LinkedList):
        pass
    else:
        return False
    
    if  llist.head == None:
        return False
    
    # Convert linked list to a Python list for easy comparison
    my_list = []
    current = llist.head
    while current:
        my_list.append(current.data)
        current = current.next

    # Check if the list is a palindrome
    rev_list = list(reversed(my_list))
    print(my_list)
    print(rev_list)
    if my_list == my_list[::-1]:
        return True
    else:
        return False