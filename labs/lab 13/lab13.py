
class HashTable:
    def __init__(self, capacity=10):
        #Task1: Define the constructor class for the HashTable
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

        

    def simple_hash(self, key):
        #Tasks2: Write the mathematical hash function that converts a key into an index integer
        """Calculate hash index using the sum of ASCII values of the key."""
        str(key)
        hash_index = 0
        for character in key:
            hash_index += ord(character)

        return int(hash_index % self.capacity)

    
    def insert(self, key, value):
        #Task3: Write the insert function that with get the index of the key then input the value
        """Insert a key-value pair into the hash table."""
        print("Key: " + str(key))
        print("Value: " + str(value))
        hash_index = self.simple_hash(key)
        print("hash index: " + str(hash_index))
        # Check for an existing key and update
        for item in self.table[hash_index]:
            if item[0] == key:
                item[1] = value
                self.check_load_factor()
                return
        # Otherwise, append new key-value pair
        self.table[hash_index].append([key, value])
        self.size += 1 # Update size
        self.check_load_factor()
        

    def search(self, key):
        #Task4: Write the search function that with take the key and retrieve the value
        """Search for a key in the hash table and return its value if found."""
        
        print("Search Table")
        for i in self.table:
            print(i)
            
        hash_index = self.simple_hash(key)
        for item in self.table[hash_index]:
            if item[0] == key:
                return item[1]

        return None  #Returns None is key not found
    

    def delete(self, key):
        #Task5: Delete the key from the hash table
        """Delete a key-value pair from the hash table."""
        hash_index = self.simple_hash(key)
        #Check if the key exists
        for item in self.table[hash_index]:
            if item[0] == key:
                self.table[hash_index].remove(item) #Delete the key from hash table
                self.size -= 1
                return True
 
        return False #Returns False if key doesn't exist
        
        
    def check_load_factor(self):
        """Check the current load factor and resize if necessary."""
        if self.size/self.capacity > 0.75:
            self.resize(2 * self.capacity)

        
    def resize(self, new_capacity):
        print("resize called")
        #Task6: Write the rehash function that will make a new table and rehash the old list contents to the new list
        """Resize the hash table to the new capacity and rehash all existing key-value pairs."""
        old_table = self.table
        print("Old Table")
        for i in self.table:
            print(i)
        self.capacity = new_capacity
        self.table = [[] for _ in range(self.capacity)]
        print("New Table")
        for i in self.table:
            print(i)
        self.size = 0  # Reset size and reinsert items
        
        for item in old_table:
            if item is not None:
                for i in item:
                    self.insert(i[0], i[1])
        
        print("New Table")
        for i in self.table:
            print(i)


# Example usage
hash_table = HashTable()
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

print(hash_table.search("key1"))  # Output: "value1"
print(hash_table.search("key3"))  # Output: "value3"

hash_table.delete("key2")
print(hash_table.search("key2"))  # Output: None

# Demonstrating resize by surpassing the load factor threshold
for i in range(4, 20):
    hash_table.insert(f"key{i}", f"value{i}")

print("After resizing:")
print(hash_table.search("key19"))  # Expected to find "value19" without performance degradation
