class BinaryTree:
    # Initialization case
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Add a node to the correct branch of the binary tree
    def add(self, value):
        # Base case for placing the overall root
        if self.value is None:  # In this case, we are adding the root
            self.value = value
        # Otherwise insert the value into the correct tree location
        else:
            self.insert(self, value)

    # Recursively iterate through the tree to find the correct location to add the value
    def insert(self, root, value):
        # If we have reached an empty node, place the value at that node
        if root is None:
            return BinaryTree(value)
        else:
            # If value is less than root.value, then traverse in the left direction
            if value < root.value:
                if root.left is None:
                    root.left = BinaryTree(value)
                else:
                    self.insert(root.left, value)
            # If value is greater than root.value, then traverse in the right direction
            else:
                if root.right is None:
                    root.right = BinaryTree(value)
                else:
                    self.insert(root.right, value)
        return root

def main():
    # Create a new binary tree
    bt = BinaryTree()

    # Add values to the tree
    bt.add(10)
    bt.add(5)
    bt.add(15)

    # Print the root and its children
    print(bt.value)      # 10
    print(bt.left.value) # 5
    print(bt.right.value) # 15

#If there is a main method, run it
if __name__ == "__main__":
    main()
