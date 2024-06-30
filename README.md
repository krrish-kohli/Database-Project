# Database Projects (Library & Calculator)

This repository contains various programs named after the different types of databases. Each program is implemented in Python and aims to create the desired output using different types of databases in each program.

## Table of Contents

- Array_Based_Lists
- Binary_Heaps
- Binary_Trees
- Chained_Hash_Table
- Graphs
- Linked_Lists
- Sorting_and_Searching


## Array_Based_Lists

## Introduction

This project implements array-based list data structures and applies them to two practical applications: a Calculator System and a Bookstore System. The project aims to develop problem-solving skills, compare different data structure implementations, and apply fundamental data structures in real-life applications.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Calculator System

- **Balanced Parentheses Checker**: A function to check whether a mathematical expression has balanced parentheses.

### Bookstore System

- **Load Product Database**: Load a product database into a catalog.
- **Search Items**: Search for items by catalog index or title infix.
- **Add Items**: Add new items to the catalog.
- **Remove Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove existing items in FIFO order.

## Data Structure Implementations

- **ArrayStack**: Implements the List and Stack interfaces.
- **ArrayQueue**: Implements the Queue interface.
- **ArrayList**: Implements the List interface.

## File Descriptions

- `ArrayStack.py`: Contains the ArrayStack class.
- `ArrayQueue.py`: Contains the ArrayQueue class.
- `ArrayList.py`: Contains the ArrayList class.
- `Calculator.py`: Contains the `balanced_parens` function.
- `BookStore.py`: Contains methods to manage the bookstore catalog and shopping cart.
- `main.py`: Main menu for navigating the application.
- `tester.py`: Contains test functions for the data structures.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd array-based-lists-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Use the main menu to select the desired application:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Calculator
        2. Bookstore System
        3. Run your own tester
        Q. Quit
    Enter your selection: 
    ```

### Calculator System

1. Select option `1` in the main menu to access the Calculator System.
2. Follow the prompts to check if a mathematical expression has balanced parentheses.

### Bookstore System

1. Select option `2` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the catalog, search for books, add to/remove from the catalog, and manage the shopping cart:

    ```plaintext
    ----------------------------------------
        BOOKSTORE MENU
        1. Load book catalog
        2. Edit the book catalog
        3. Access book at index
        4. Search book by infix
        5. Add a book by index to shopping cart
        6. Remove from the shopping cart
        Q. Return to main menu
    ----------------------------------------
    ```

## Testing

1. Run the `tester.py` script to test the data structures:
    ```bash
    python main.py
    ```
2. Select option `3` in the main menu to run the tester.

#
#
  

## Binary_Heaps

## Introduction

This project implements various data structures and demonstrates their applications through a library system and a calculator model. The library system manages a catalog of books, while the calculator ensures balanced parentheses in mathematical expressions.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Library System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Data Structure Implementations

- **ArrayList**: Implements a dynamic array-based list.
- **BinaryHeap**: Implements a binary heap for priority queue operations.
- **BinarySearchTree**: Implements a binary search tree for efficient data retrieval.
- **BinaryTree**: Base class for binary tree structures.
- **ChainedHashTable**: Implements a hash table with chaining for collision resolution.
- **DLLDeque**: Implements a double-ended queue using a doubly linked list.
- **DLList**: Implements a doubly linked list.
- **Interfaces**: Contains interface definitions for various data structures.
- **MaxQueue**: Implements a queue with maximum value retrieval.
- **SLLQueue**: Implements a singly linked list-based queue.
- **SLLStack**: Implements a singly linked list-based stack.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of the library system and calculator.
- `ArrayList.py`: Contains the ArrayList class.
- `BinaryHeap.py`: Contains the BinaryHeap class.
- `BinarySearchTree.py`: Contains the BinarySearchTree class.
- `BinaryTree.py`: Contains the BinaryTree base class.
- `Book.py`: Contains the Book class.
- `BookStore.py`: Implements the bookstore system using ArrayList and other data structures.
- `Calculator.py`: Implements the balanced parentheses checker.
- `ChainedHashTable.py`: Contains the ChainedHashTable class.
- `DLLDeque.py`: Contains the DLLDeque class.
- `DLList.py`: Contains the DLList class.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Contains the MaxQueue class.
- `SLLQueue.py`: Contains the SLLQueue class.
- `SLLStack.py`: Contains the SLLStack class.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd library-and-calculator-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform library and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Calculator
        2. Bookstore System
        Q. Quit
    Enter your selection: 
    ```

### Calculator

1. Select option `1` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

### Bookstore System

1. Select option `2` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each data structure and application.

#
#

## Binary_Trees

## Introduction

This project focuses on the implementation and application of various binary tree structures. It includes a bookstore system that manages a catalog of books and a calculator system that checks for balanced parentheses in mathematical expressions.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Library System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Data Structure Implementations

- **BinarySearchTree**: Implements a binary search tree for efficient data retrieval.
- **BinaryTree**: Base class for binary tree structures.
- **ArrayList**: Implements a dynamic array-based list.
- **ChainedHashTable**: Implements a hash table with chaining for collision resolution.
- **DLLDeque**: Implements a double-ended queue using a doubly linked list.
- **DLList**: Implements a doubly linked list.
- **MaxQueue**: Implements a queue with maximum value retrieval.
- **SLLQueue**: Implements a singly linked list-based queue.
- **SLLStack**: Implements a singly linked list-based stack.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of the library system and calculator.
- `ArrayList.py`: Contains the ArrayList class.
- `BinarySearchTree.py`: Contains the BinarySearchTree class.
- `BinaryTree.py`: Contains the BinaryTree base class.
- `Book.py`: Contains the Book class.
- `BookStore.py`: Implements the bookstore system using ArrayList and other data structures.
- `Calculator.py`: Implements the balanced parentheses checker.
- `ChainedHashTable.py`: Contains the ChainedHashTable class.
- `DLLDeque.py`: Contains the DLLDeque class.
- `DLList.py`: Contains the DLList class.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Contains the MaxQueue class.
- `SLLQueue.py`: Contains the SLLQueue class.
- `SLLStack.py`: Contains the SLLStack class.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd binary-trees-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform library and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Calculator
        2. Bookstore System
        Q. Quit
    Enter your selection: 
    ```

### Calculator

1. Select option `1` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

### Bookstore System

1. Select option `2` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each data structure and application.

#
#

## Chained_Hash_Table

## Introduction

This project focuses on the implementation and application of a Chained Hash Table, along with other essential data structures. It includes a bookstore system that manages a catalog of books and a calculator system that checks for balanced parentheses in mathematical expressions.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Library System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Data Structure Implementations

- **ChainedHashTable**: Implements a hash table with chaining for collision resolution.
- **ArrayList**: Implements a dynamic array-based list.
- **DLLDeque**: Implements a double-ended queue using a doubly linked list.
- **DLList**: Implements a doubly linked list.
- **MaxQueue**: Implements a queue with maximum value retrieval.
- **SLLQueue**: Implements a singly linked list-based queue.
- **SLLStack**: Implements a singly linked list-based stack.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of the library system and calculator.
- `ArrayList.py`: Contains the ArrayList class.
- `Book.py`: Contains the Book class.
- `BookStore.py`: Implements the bookstore system using ArrayList and other data structures.
- `Calculator.py`: Implements the balanced parentheses checker.
- `ChainedHashTable.py`: Contains the ChainedHashTable class.
- `DLLDeque.py`: Contains the DLLDeque class.
- `DLList.py`: Contains the DLList class.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Contains the MaxQueue class.
- `SLLQueue.py`: Contains the SLLQueue class.
- `SLLStack.py`: Contains the SLLStack class.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd chained-hash-table-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform library and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Calculator
        2. Bookstore System
        Q. Quit
    Enter your selection: 
    ```

### Calculator

1. Select option `1` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

### Bookstore System

1. Select option `2` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each data structure and application.

#
#

## Graphs

## Introduction

This project focuses on implementing essential graph data structures and other fundamental data structures for practical applications. It includes systems for managing books in a bookstore and evaluating mathematical expressions for balanced parentheses.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Bookstore System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Data Structure Implementations

- **AdjacencyList**: Implements a graph using adjacency list representation.
- **AdjacencyMatrix**: Implements a graph using adjacency matrix representation.
- **ArrayList**: Implements a dynamic array-based list.
- **ArrayQueue**: Implements a queue using an array-based list.
- **ArrayStack**: Implements a stack using an array-based list.
- **BinaryHeap**: Implements a binary heap for priority queue operations.
- **BinarySearchTree**: Implements a binary search tree for efficient data retrieval.
- **BinaryTree**: Base class for binary tree structures.
- **Book**: Defines the Book class for the bookstore system.
- **BookStore**: Implements the bookstore system using ArrayList and other data structures.
- **Calculator**: Implements the balanced parentheses checker for mathematical expressions.
- **ChainedHashTable**: Implements a hash table with chaining for collision resolution.
- **DLLDeque**: Implements a double-ended queue using a doubly linked list.
- **DLList**: Implements a doubly linked list.
- **MaxQueue**: Implements a queue with maximum value retrieval.
- **SLLQueue**: Implements a singly linked list-based queue.
- **SLLStack**: Implements a singly linked list-based stack.
- **SortableBook**: Extension of Book class for sortable properties.
- **algorithms**: Contains various algorithms used in the project.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of the bookstore system and calculator.
- `AdjacencyList.py`: Implements a graph using adjacency list representation.
- `AdjacencyMatrix.py`: Implements a graph using adjacency matrix representation.
- `ArrayList.py`: Implements a dynamic array-based list.
- `ArrayQueue.py`: Implements a queue using an array-based list.
- `ArrayStack.py`: Implements a stack using an array-based list.
- `BinaryHeap.py`: Implements a binary heap for priority queue operations.
- `BinarySearchTree.py`: Implements a binary search tree for efficient data retrieval.
- `BinaryTree.py`: Base class for binary tree structures.
- `Book.py`: Defines the Book class for the bookstore system.
- `BookStore.py`: Implements the bookstore system using ArrayList and other data structures.
- `Calculator.py`: Implements the balanced parentheses checker for mathematical expressions.
- `ChainedHashTable.py`: Implements a hash table with chaining for collision resolution.
- `DLLDeque.py`: Implements a double-ended queue using a doubly linked list.
- `DLList.py`: Implements a doubly linked list.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Implements a queue with maximum value retrieval.
- `SLLQueue.py`: Implements a singly linked list-based queue.
- `SLLStack.py`: Implements a singly linked list-based stack.
- `SortableBook.py`: Extension of Book class for sortable properties.
- `algorithms.py`: Contains various algorithms used in the project.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd graphs-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform bookstore and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Bookstore System
        2. Calculator
        Q. Quit
    Enter your selection: 
    ```

### Bookstore System

1. Select option `1` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

### Calculator

1. Select option `2` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each data structure and application.

#
#

## Linked_Lists


## Introduction

This project implements various types of linked lists and applies them to practical applications such as managing books in a bookstore and evaluating mathematical expressions for balanced parentheses.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 3**: Develop problem-solving skills by implementing data structures.
- **CLO 4**: Compare advantages and disadvantages of different data structure implementations.

## Features

### Bookstore System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Data Structure Implementations

- **SinglyLinkedList (SLL)**: Implements a singly linked list.
- **DoublyLinkedList (DLL)**: Implements a doubly linked list.
- **ArrayList**: Implements a dynamic array-based list.
- **MaxQueue**: Implements a queue with maximum value retrieval.
- **SLLQueue**: Implements a queue using a singly linked list.
- **SLLStack**: Implements a stack using a singly linked list.
- **Book**: Defines the Book class for the bookstore system.
- **BookStore**: Implements the bookstore system using linked lists and other data structures.
- **Calculator**: Implements the balanced parentheses checker for mathematical expressions.
- **Interfaces**: Defines interfaces for various data structures.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of the bookstore system and calculator.
- `ArrayList.py`: Implements the ArrayList class.
- `Book.py`: Defines the Book class for the bookstore system.
- `BookStore.py`: Implements the bookstore system using linked lists and other data structures.
- `Calculator.py`: Implements the balanced parentheses checker for mathematical expressions.
- `DLLDeque.py`: Implements a double-ended queue using a doubly linked list.
- `DLList.py`: Implements a doubly linked list.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Implements a queue with maximum value retrieval.
- `SLLQueue.py`: Implements a queue using a singly linked list.
- `SLLStack.py`: Implements a stack using a singly linked list.
- `books.txt`: A text database of books for testing.
- `booktest.txt`: A smaller text database of books for testing.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd linked-lists-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform bookstore and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Bookstore System
        2. Calculator
        Q. Quit
    Enter your selection: 
    ```

### Bookstore System

1. Select option `1` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

### Calculator

1. Select option `2` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each data structure and application.

#
#

## Sorting_and_Searching

## Introduction

This project implements sorting and searching algorithms using various data structures and applies them to manage books in a bookstore and evaluate mathematical expressions for balanced parentheses.

## Learning Objectives

- **CLO 1**: Identify fundamental data structures in computer science and their use in real-life applications.
- **CLO 2**: Implement sorting and searching algorithms efficiently.
- **CLO 3**: Develop problem-solving skills by applying algorithms to practical scenarios.

## Features

### Bookstore System

- **Load Book Catalog**: Load a product database into a catalog.
- **Search by Index**: Search for items via catalog index.
- **Search by Title Infix**: Search for items by title infix.
- **Add New Items**: Add new items to the catalog.
- **Delete Items**: Remove existing items from the catalog.
- **Shopping Cart**: Add items to a shopping cart and remove them in FIFO order.

### Calculator

- **Balanced Parentheses**: Check if a mathematical expression has balanced parentheses.

## Sorting and Searching Implementations

- **Sorting Algorithms**:
  - **Bubble Sort**: Implements the bubble sort algorithm.
  - **Insertion Sort**: Implements the insertion sort algorithm.
  - **Selection Sort**: Implements the selection sort algorithm.
  - **Merge Sort**: Implements the merge sort algorithm.
  - **Quick Sort**: Implements the quick sort algorithm.
  
- **Searching Algorithms**:
  - **Binary Search**: Implements the binary search algorithm.
  - **Linear Search**: Implements the linear search algorithm.
  - **Interpolation Search**: Implements the interpolation search algorithm.

## File Descriptions

- `main.py`: Main program to demonstrate the functionality of sorting, searching, bookstore system, and calculator.
- `ArrayList.py`: Implements the ArrayList class.
- `BinaryHeap.py`: Contains the BinaryHeap class.
- `BinarySearchTree.py`: Contains the BinarySearchTree class.
- `BinaryTree.py`: Contains the BinaryTree base class.
- `Book.py`: Defines the Book class for the bookstore system.
- `BookStore.py`: Implements the bookstore system using various data structures.
- `Calculator.py`: Implements the balanced parentheses checker.
- `ChainedHashTable.py`: Contains the ChainedHashTable class.
- `DLLDeque.py`: Implements a double-ended queue using a doubly linked list.
- `DLList.py`: Implements a doubly linked list.
- `Interfaces.py`: Defines interfaces for various data structures.
- `MaxQueue.py`: Implements a queue with maximum value retrieval.
- `SLLQueue.py`: Implements a queue using a singly linked list.
- `SLLStack.py`: Implements a stack using a singly linked list.
- `SortableBook.py`: Contains the SortableBook class for sorting operations.
- `algorithms.py`: Implements sorting and searching algorithms.
- `books_1.txt`, `books_2.txt`, `books_3.txt`: Text databases of books for testing.
- `exceptions.py`: Contains custom exception classes.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd sorting-searching-project
    ```

## Usage

1. Run the main program:
    ```bash
    python main.py
    ```
2. Follow the prompts to perform sorting, searching, bookstore, and calculator operations:

    ```plaintext
    ----------------------------------------
        MAIN MENU
        1. Sorting and Searching
        2. Bookstore System
        3. Calculator
        Q. Quit
    Enter your selection: 
    ```

### Sorting and Searching

1. Select option `1` in the main menu to access Sorting and Searching.
2. Use the sub-menu options to choose and execute sorting and searching algorithms.

### Bookstore System

1. Select option `2` in the main menu to access the Bookstore System.
2. Use the sub-menu options to load the book catalog, search for books, add or remove books, and manage the shopping cart.

### Calculator

1. Select option `3` in the main menu to access the Calculator.
2. Use the sub-menu options to check if a mathematical expression has balanced parentheses.

## Testing

1. Ensure all functionalities are tested thoroughly before submitting.
2. Use `tester.py` (if available) or create your own tests to verify the correctness of each algorithm and application.

