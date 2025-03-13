#Main method file that utilizes the Tree class found in Tree.py
#Adds extra functionality of allowing the user to see if a specific int is in the generated tree
#This file has no error checking if the user inputs a value that isa non-int as this is meant to only be a demo of the binary search tree data type
import random
from Tree import Tree
def main():
    #Create and fill a randomly generated tree
    randomTree = Tree()
    valueCount = 10
    print("Inserting the following values:")
    while valueCount > 0:
        randomTree.insert_node(random.randint(0, 99))
        valueCount -= 1

    continueGame = True    
    #While the user still wants to play the game
    while continueGame is True:
        #Print the array and ask the user for an interger to find an index of
        randomTree.preorder_traversal()
        #No error correction as this is meant to be a demo program (only takes integers)
        userInput = int(input("\nPlease enter an integer value to see if the tree contains it (-1 to quit): "))
        
        #If user is done playing game
        if userInput == -1:
            continueGame = False
        #Else search the tree to see if it contains the users input
        else:
            contains = randomTree.contains(userInput)
            if contains is None:
                print(f"The tree does not contain {userInput}\n")
            else:
                print(f"The tree contains {userInput}\n")

if __name__ == "__main__":
    main()