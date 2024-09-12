class TreeNode:
    def __init__(self, name, isFile=False):
        # The name attribute represents the name of the file or directory.
        # The isFile attribute is a boolean indicating whether the node is a file (True) or directory (False).

        # The children attribute holds a list of TreeNode objects representing the node's children.
        # This is where the N-ary tree structure comes into play, allowing each node to have multiple children.
        # This should be initialized as an empty list.
        self.name = name
        self.isFile = isFile
        self.children = []


class FileExplorer:
    def __init__(self):
        self.root = TreeNode("/", isFile=False)

    def _find_child(self, parent, name):
        """Helper method to find a child node by name under the given parent.
        - Iterate through the parent's children list.
        - If a child with the specified name is found, return the child TreeNode.
        - Otherwise, return None to indicate the child does not exist.
        """
        if parent: #Checks that the parent node is not None#
            for child in parent.children:
                if child.name == name:
                    return child

        return None

    def search(self, path):
        path_parts = path.strip("/").split("/")
        current = self.root
        for part in path_parts:
            """Search for a node by its path.
            - Split the path string into components based on slashes (/).
            - Traverse the tree from the root, following the path components.
            - If the traversal is successful and the target node is found, return the node.
            - If any part of the path cannot be followed (e.g., a directory does not exist), return None.
            """
            if self._find_child(current, part) != None:
                current = self._find_child(current, part)
            else:
                return None
            
        return current

    def insert(self, path, isFile=False):
        path_parts = path.strip("/").split("/")
        current = self.root
        print(current.name)
        for part in path_parts[:-1]: #Iterates through all but the last node path#
            """Insert a new file or directory at the specified path.
            - Similar to search, split the path and traverse the tree to find where the new node should be inserted.
            - If part of the path does not exist (e.g., intermediate directories), create these directories as needed.
            - Check if the final node already exists to avoid duplicates. If it does not exist, insert the new node.
            - Consider the isFile flag to correctly set the node as a file or directory.
            """
            if self._find_child(current, part) != None:
                print(current.name)
                current = self._find_child(current, part)
                print(current.name)
            else: #Adds a new intermediate directory#
                print("Adding new intermediate directory")
                current.children.append(TreeNode(part, isFile=False)) #Must be a directory, because it isn't the last node#
                print(current.name)
                current = self._find_child(current, part)

        if self._find_child(current, path_parts[-1]) == None: #Adds as child of the correct directory if there's NO duplicates#
            current.children.append(TreeNode(path_parts[-1], isFile)) #Must be a directory, because it isn't the last node#
            print(current.name)

    def delete(self, path):
        path_parts = path.strip("/").split("/")
        parent = self.search("/".join(path_parts[:-1]))
        print(parent.name)
        print(parent.children)
        """Delete a node specified by the path.
        - Find the node to be deleted and its parent using a similar traversal method as in search.
        - Remove the target node from the parent's children list.
        - Special consideration is needed if the target is a directory with its own children.
        """
        for child in parent.children:
            if child.name == path_parts[-1]: #If the child is the child to be deleted#
                if child.isFile: #Removes child if it's a file#
                    parent.children.remove(child)
                elif not child.isFile: #If child is a directory, removes all the child's children then removes the child itself#
                    for c in child.children:
                        child.children.remove(c)
                    parent.children.remove(child)


    def move(self, source_path, destination_path):
        """Move a node from the source path to the destination path.
        - This involves finding the node at the source path, removing it, and then re-inserting it at the destination path.
        - Ensure the moved node retains its original properties, such as isFile, name, and children.
        - The destination path may require creating new directories.
        """
        self.delete(source_path)
        self.insert(destination_path)
        
# Example Usage
explorer = FileExplorer()
explorer.insert("home/documents/lab/lab12.py", isFile=True)
explorer.insert("home/music")

print(explorer.search("home/documents/lab/lab12.py") is not None)  # True
print(explorer.search("home/music") is not None)  # True

explorer.delete("home/documents/lab/lab12.py")
print(explorer.search("home/documents/lab/lab12.py") is not None)  # False

explorer.move("home/music", "home/documents/music")
print(explorer.search("home/music") is not None)  # False
print(explorer.search("home/documents/music") is not None)  # True