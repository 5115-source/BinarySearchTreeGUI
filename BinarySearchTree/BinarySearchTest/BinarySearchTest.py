#I used ChatGPT to quickly translate the base java demo code into python for this project.
#When translating ChatGPT decided to complete the program for me.
#But I deleted that code and rewrote the main method myself for better understanding of the concepts.
#This allowed for better commenting on the functionality of the code, and a flow that I understand better.
import random

# perform a binary search on the data
def binary_search(data, key):
    low = 0  # low end of the search area
    high = len(data) - 1  # high end of the search area
    location = -1  # return value; -1 if not found

    while low <= high and location == -1:
        # calculate middle element
        middle = (low + high) // 2
        
        # print remaining elements of array
        print(remaining_elements(data, low, high))

        # output spaces for alignment
        for i in range(middle):
            print("   ", end="")
        print(" * ")  # indicate current middle

        # if the element is found at the middle
        if key == data[middle]:
            location = middle  # location is the current middle
        elif key < data[middle]:  # middle element is too high
            high = middle - 1  # eliminate the higher half
        else:  # middle element is too low
            low = middle + 1  # eliminate the lower half

    return location  # return location of search key

# method to output certain values in array
def remaining_elements(data, low, high):
    # append spaces for alignment
    temporary = ""

    for i in range(low):
        temporary += "   "

    # append elements left in array
    for i in range(low, high + 1):
        temporary += f"{data[i]} "

    return temporary + "\n"

def main():
    # Create array of 15 random integers in sorted order
    intArray = sorted(random.sample(range(0, 99), 15))
    continueGame = True
    
    #While the user still wants to play the game
    while continueGame is True:
        #Print the array and ask the user for an interger to find an index of
        print(f"{intArray}\n")
        #No error correction as this is meant to be a demo program (only takes integers)
        userInput = int(input("Please enter an integer value (-1 to quit): "))
        
        #If user is done playing game
        if userInput == -1:
            continueGame = False
        #Else search the tree for the index of the users input
        else:
            findValue = binary_search(intArray, userInput)
            if findValue == -1:
                print(f"{userInput} was not found.\n")
            else:
                print(f"{userInput} was found at index {findValue}.\n")

if __name__ == "__main__":
    main()