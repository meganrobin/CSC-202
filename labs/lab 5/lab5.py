class Node:
    """ 
    A node in a doubly linked list.

    Attributes:
        data: The data stored in the node.
        prev: A pointer to the previous node in the list.
        next: A pointer to the next node in the list.
    """
    def __init__(self, data):
        """
        Initializes a new node.

        Parameters:
            data: The data to store in the node.
        """
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """ 
    A doubly linked list.

    Attributes:
        head: The first node in the list.
    """
    def __init__(self):
        """ Initializes an empty doubly linked list. """
        self.head = None

    def append(self, data):
        """
        Appends a new node with the specified data to the end of the list.

        Parameters:
            data: The data to be added to the list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def __eq__(self, other):
        """
        Checks if the current list is equal to another list.

        Parameters:
            other: The list to compare with.

        Returns:
            True if the lists are equal, False otherwise.
        """
        if not isinstance(other, DoublyLinkedList):
            return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self == current_other

    def __getitem__(self, index):
        """
        Gets the data of the node at the specified index.

        Parameters:
            index: The index of the node.

        Returns:
            The data of the node at the specified index.

        Raises:
            TypeError: If the index is not an integer.
            ValueError: If the index is negative.
            IndexError: If the index is out of range of the list.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def __setitem__(self, index, data):
        """
        Sets the data of the node at the specified index.

        Parameters:
            index: The index of the node where the data is to be set.
            data: The data to set at the specified index.

        Raises:
            TypeError: If the index is not an integer.
            ValueError: If the index is negative.
            IndexError: If the index is out of range of the list.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        current.data = data

    def __str__(self):
        """
        String representation of the doubly linked list.

        Returns:
            A string representing the list elements.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' <-> '.join(result)
