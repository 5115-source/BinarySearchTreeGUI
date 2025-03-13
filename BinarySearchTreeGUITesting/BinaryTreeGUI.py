import tkinter as tk

#Create a simple binary tree class to utilize
class BinaryTree:
    #Initialization case
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        
    #Add a node to the correct branch of the binary tree
    def add(self, value):
        #Base case for placing the overall root
        if self.value is None:
            self.value = value
        #Otherwise insert the value into the correct tree location
        else:
            self.insert(self, value)
        
    #recursivly iterate through the tree to find the correct location to add the value
    def insert(self, root, value):
        #If we have reached an empty node place the value at that node
        if root is None:
            return BinaryTree(value)
        else:
            #If value is less than the value of the root then traverse in the left direction
            if value < root.value:
                #If the node to the left is empty then add the current value
                if root.left is None:
                    root.left = BinaryTree(value)
                #Make the current left node the root to iterate through the tree further
                else:
                    self.insert(root.left, value)
                    
            #If value is greater than the value of the root then traverse in the right direction
            else:
                #If the node to the right is empty then add the current value
                if root.right is None:
                    root.right = BinaryTree(value)
                #Make the current right node the root to iterate through the tree further
                else:
                    self.insert(root.right, value)
        #Return the root to the add method???
        return root

#Create a class to correctly print a GUI of the binary tree
class PrintBinarySearchTree:
    def test():
        print()
        
#Main method that calls sub methods to organize game logic and allow to play the game
def main():
    
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting = tk.Label(text="Hello, Tkinter")
    
    rootTest = 50
    bt = BinaryTree()
    #Testing adding nodes and using the add portion of the class
    for value in [50, 30, 20, 40, 70, 60, 80]:
        
        bt.add(value)
    
    print(bt.value)      # 10
    print(bt.left.value) # 5
    print(bt.right.value) # 15
    
    userInput()
    printTree()
    
#Ask for user input for values to create a tree with
def userInput():
    #print a user input panel that gives the user the option for 3 overall roots and 3 sets of values to add to the tree
    
    #Take the user input and make a binary tree
    
    #Return the binary tree for future printing
    print()
    
#Print the binary search tree in a formatted way
def printTree():
    #Use a while loop to iterate through the tree until we reach a node of None
    print()
    
def searchTree():
    #Should I make a search function into this program that searches through the tree for a specified value?
    print()
    
#If there is a main method, run it
if __name__ == "__main__":
    main()
