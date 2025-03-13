This repo is a collection of GUI test programs when I wanted to make a GUI program representing a binary search tree. But it is also a demo of using a binary search tree in different cases. All finished non GUI programs have the added functionality of asking for user input, but no proper input checker to see if the user inputteed an int as these are meant to be data type demo programs.

The repo is organized into a somewhat organized file directory.
 - The [BinarySearchTreeGUITesting](https://github.com/5115-source/BinarySearchTreeGUI/tree/main/BinarySearchTreeGUITesting) folder is a massive compilation of test files with varying successes of integrating tkinter into python to represent a binary search tree graphically. This ended up wasting a lot of time, and I just needed to focus on getting working non GUI programs.

 - The [BinarySearchTree folder](https://github.com/5115-source/BinarySearchTreeGUI/tree/main/BinarySearchTree) contains two programs.
    - The [TreeTest folder](https://github.com/5115-source/BinarySearchTreeGUI/tree/main/BinarySearchTree/TreeTest) contains the [TreeTest](https://github.com/5115-source/BinarySearchTreeGUI/blob/main/BinarySearchTree/TreeTest/TreeTest.py) binary search tree demo program which relies on the [Tree](https://github.com/5115-source/BinarySearchTreeGUI/blob/main/BinarySearchTree/TreeTest/Tree.py) class to function. The [Tree](https://github.com/5115-source/BinarySearchTreeGUI/blob/main/BinarySearchTree/TreeTest/Tree.py) class was originally written in java and was translated to python using ChatGPT.

    - The [BinarySearchTest folder](https://github.com/5115-source/BinarySearchTreeGUI/tree/main/BinarySearchTree) contains the [BinarySearchTest](https://github.com/5115-source/BinarySearchTreeGUI/blob/main/BinarySearchTree/BinarySearchTest/BinarySearchTest.py) program which visualizes a search from a randomly generated binary tree to see if it contains a user chosen integer.