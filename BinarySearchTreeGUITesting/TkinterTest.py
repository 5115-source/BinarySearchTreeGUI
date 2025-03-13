import tkinter as tk

# Binary Search Tree Class
class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def add(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self.insert(self.root, key)

    # Function to return the positions of nodes for drawing
    def get_positions(self, node, x, y, level, positions):
        if node is not None:
            positions.append((node.val, x, y))  # Save node value and coordinates
            offset = 100 / (level + 1)
            self.get_positions(node.left, x - offset, y + 100, level + 1, positions)
            self.get_positions(node.right, x + offset, y + 100, level + 1, positions)

# Tkinter Application Class
class BSTVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Binary Search Tree Visualizer")
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()
        
        self.bst = BST()
        self.node_radius = 20

        # Add some initial nodes
        for value in [50, 30, 20, 40, 70, 60, 80, 90, 70, 100, 140, 20, 10, 50, 30, 20]:
            self.bst.add(value)

        # Draw the initial tree
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")  # Clear canvas before redrawing
        positions = []
        self.bst.get_positions(self.bst.root, 400, 50, 0, positions)

        # Draw the nodes
        for value, x, y in positions:
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius, 
                                    x + self.node_radius, y + self.node_radius, 
                                    fill="lightblue", outline="black")
            self.canvas.create_text(x, y, text=str(value))

        # Draw the edges
        for value, x, y in positions:
            node = self.find_node(self.bst.root, value)
            if node.left:
                left_x = x - 100 / (self.get_level(self.bst.root, node.left) + 1)
                left_y = y + 100
                self.canvas.create_line(x, y, left_x, left_y)
            if node.right:
                right_x = x + 100 / (self.get_level(self.bst.root, node.right) + 1)
                right_y = y + 100
                self.canvas.create_line(x, y, right_x, right_y)

    def find_node(self, root, value):
        if root is None or root.val == value:
            return root
        elif value < root.val:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)

    def get_level(self, root, node, level=0):
        if root is None:
            return -1
        if root == node:
            return level
        left_level = self.get_level(root.left, node, level + 1)
        if left_level != -1:
            return left_level
        return self.get_level(root.right, node, level + 1)

# Run the GUI application
if __name__ == "__main__":
    app = BSTVisualizer()
    app.mainloop()
