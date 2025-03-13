#I used ChatGPT to quickly translate the java version of this class into python for this project.

# TreeNode class definition
class TreeNode:
    def __init__(self, node_data):
        self.data = node_data  # node value
        self.left_node = None  # left child
        self.right_node = None  # right child

    def insert(self, insert_value):
        # Insert in left subtree
        if insert_value < self.data:
            if self.left_node is None:
                self.left_node = TreeNode(insert_value)
            else:
                self.left_node.insert(insert_value)
        # Insert in right subtree
        elif insert_value > self.data:
            if self.right_node is None:
                self.right_node = TreeNode(insert_value)
            else:
                self.right_node.insert(insert_value)

# Tree class definition
class Tree:
    def __init__(self):
        self.root = None  # Root node is initially None

    def insert_node(self, insert_value):
        if self.root is None:
            self.root = TreeNode(insert_value)  # Create root node
        else:
            self.root.insert(insert_value)  # Insert recursively

    def preorder_traversal(self):
        self._preorder_helper(self.root)

    def _preorder_helper(self, node):
        if node is None:
            return
        print(node.data, end=" ")  # Output node data
        self._preorder_helper(node.left_node)  # Traverse left subtree
        self._preorder_helper(node.right_node)  # Traverse right subtree

    def inorder_traversal(self):
        self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        if node is None:
            return
        self._inorder_helper(node.left_node)  # Traverse left subtree
        print(node.data, end=" ")  # Output node data
        self._inorder_helper(node.right_node)  # Traverse right subtree

    def postorder_traversal(self):
        self._postorder_helper(self.root)

    def _postorder_helper(self, node):
        if node is None:
            return
        self._postorder_helper(node.left_node)  # Traverse left subtree
        self._postorder_helper(node.right_node)  # Traverse right subtree
        print(node.data, end=" ")  # Output node data

    def contains(self, value):
        current = self.root
        while current is not None:
            if value < current.data:
                current = current.left_node  # Search left subtree
            elif value > current.data:
                current = current.right_node  # Search right subtree
            else:
                return current.data  # Element found
        return None  # Element not found
