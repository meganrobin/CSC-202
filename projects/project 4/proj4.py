class Hashtable:
    """A simple hashtable implementation using linear probing for collision resolution.

    Attributes:
        capacity (int): The maximum number of items that can be stored in the hashtable.
        table (list): The underlying data structure for storing items in the hashtable.
        size (int): The current number of items stored in the hashtable.
    """

    def __init__(self, capacity=12):
        """Initialize a new Hashtable instance.

        Args:
            capacity (int): The maximum capacity of the hashtable. Default is 12.
        """
        self.capacity = capacity
        self.table = [None for _ in range(capacity)]
        self.size = 0

    def hash(self, key):
        """Generate a hash value for a given key.

        Args:
            key (str): The key to hash. Must be a single character.

        Returns:
            int: The hash value of the key, determined by its ASCII value modulo the capacity.

        Raises:
            ValueError: If the key is not a single character.
        """
        if len(key) != 1:
            raise ValueError("Key must be a single character.")
        return ord(key) % self.capacity

    def insert(self, key, value):
        """Insert a key-value pair into the hashtable.

        Uses linear probing to resolve collisions. If the key already exists, its value is updated.

        Args:
            key (str): The key to insert. Must be a single character.
            value: The value associated with the key.

        Raises:
            Exception: If the hashtable is full and cannot accommodate more items.
        """
        position = self.hash(key)
        original_position = position

        while self.table[position] is not None:
            if self.table[position][0] == key:
                print("KEY: ")
                print(self.table[position][0])
                self.table[position][1] = value
                return
            position = (position + 1) % self.capacity
            if position == original_position:
                print("position:" +str(original_position) + str(position))
                raise Exception("Hash table is full")
        self.table[position] = [key, value]
        print(self.table[position])
        print(self.table)
        self.size += 1



    def get(self, key):
        """Retrieve the value associated with a given key.

        Args:
            key (str): The key whose value is to be retrieved.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        position = self.hash(key)
        original_position = position
        while True:
            if self.table[position] is None:
                if position == original_position:
                    print(position)
                    print(original_position)

                    print("first none")
                    return None
                position = (position + 1) % self.capacity
            if self.table[position][0] == key:
                return self.table[position][1]
            position = (position + 1) % self.capacity
            if position == original_position:
                print("second none")
                return None



    def delete(self, key):
        """Delete a key-value pair from the hashtable.

        Args:
            key (str): The key to be deleted.

        Returns:
            bool: True if the item was successfully deleted, False otherwise.
        """
        position = self.hash(key)
        original_position = position
        while True:
            if self.table[position] == None:
                if position == original_position:
                    return False
            if self.table[position][0] == key:
                self.table[position] = None
                self.size -= 1
                return True
            position = (position + 1) % self.capacity
            if position == original_position:
                break
        return False


    def print(self):
        """Print the contents of the hashtable in a readable format."""
        print("Hashtable contents:")
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: Vertex {item[0]}, Neighbors {item[1]}")
            else:
                print(f"Index {index}: Empty")


class Graph:
    """A simple undirected graph implementation using a custom hashtable for adjacency lists.

    Attributes:
        graph (Hashtable): The hashtable used to store the adjacency lists of the graph.
    """

    def __init__(self, vertices):
        """Initialize a new Graph instance.

        Args:
            vertices (int): The number of vertices in the graph, which determines the capacity of the hashtable.
        """
        self.graph = Hashtable(vertices)
    
    def add_edge(self, src, dest):
        """Add an edge between two vertices in the graph.

        This method ensures the graph remains undirected by adding an entry in both vertices' adjacency lists.

        Args:
            src (str): The source vertex.
            dest (str): The destination vertex.
        """
        # Add dest to src's adjacency list.
        neighbors = self.graph.get(src)
        if neighbors is None:
            self.graph.insert(src, [dest])
        else:
            neighbors.append(dest)
            self.graph.insert(src, neighbors)
        
        # Add src to dest's adjacency list.
        neighbors = self.graph.get(dest)
        if neighbors is None:
            self.graph.insert(dest, [src])
        else:
            neighbors.append(src)
            self.graph.insert(dest, neighbors)


    def dfs_traversal(self, start_vertex, visited=None):
        """Perform a depth-first search (DFS) traversal from a given start vertex.

        Args:
            start_vertex (str): The vertex from which the DFS traversal starts.
            visited (set, optional): A set of already visited vertices to avoid cycles. Defaults to None.

        Returns:
            set: A set of vertices that were visited during the DFS traversal.
        """
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        print(start_vertex)
        neighbors = self.graph.get(start_vertex)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dfs_traversal(neighbor, visited)

        return visited





if __name__ == "__main__":
    graph = Graph(12)  # Example capacity
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'F')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'G')

    print("DFS Traversal starting from vertex 'A':")
    graph.dfs_traversal('A')
    print()  # Newline for better readability

    # Optionally, print the graph's contents
    print("\nGraph's adjacency list:")
    graph.graph.print()