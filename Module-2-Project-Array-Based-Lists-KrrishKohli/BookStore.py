import time

import ArrayList
import ArrayQueue
import Book


class BookStore:
    """
    Simulates a book system such as Amazon. It allows  searching,
    removing and adding to a shopping cart.  New items can be added to the
    catalog.  Existing items can be removed from the catalog
    """

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()

    """ --------- METHODS RELATED TO THE CATALOG --------- """
    def loadCatalog(self, fileName: str):
        """
        reads the text file at the given directory and creates the array list with all books.
        Each book record contains a key, title, group, rank (number of copies sold) and
        a list of keys of similar books
        """
        try:
            self.bookCatalog = ArrayList.ArrayList()
            with open(fileName, encoding="utf8") as f:
                # The following line is the time that the computation starts
                start_time = time.time()
                for line in f:
                    (key, title, group, rank, similar) = line.split("^")
                    s = Book.Book(key, title, group, rank, similar)
                    self.bookCatalog.append(s)
                elapsed_time = time.time() - start_time
                print(f"Loaded {self.bookCatalog.size()} books in {elapsed_time} seconds.")
        except Exception as e:
            print("Encountered the following unexpected error while loading the catalog:\n", e)

    def addToCatalog(self, i, book : Book.Book):
        """
        inserts a new book to the catalog at the given index
        :param i: int type; the index of insertion
        :param book: Book type; the new book
        :return: None
        """
        try:
            print(f"Current catalog size: {self.bookCatalog.size()}")
            start_time = time.time()
          
            # FIXME: Complete the implementation so that the given book gets added to the book catalog
            # at the given index.
            self.bookCatalog.add(i, book)
            elapsed_time = time.time() - start_time
            print(f"Inserted the following book at index {i}:{book}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}.")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)

    def removeFromCatalog(self, i: int):
        """
        removes from the catalog the book at index i and displays its information
        :param i: int type; the index of the book to be removed
        """
        try:
            print(f"Current catalog size: {self.bookCatalog.size()}")
            start_time = time.time()
          
            # FIXME: Correct the line below
            removed_book = self.bookCatalog.remove(i)
            """FIXME: Replace this string with the correct code"""
          
            elapsed_time = time.time() - start_time
            print(f"Removed the following book from catalog:{removed_book}\nCatalog size after removal: "
                  f"{self.bookCatalog.size()}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)

    def getBookAtIndex(self, i : int):
        """
        retrieves the Book at index i of the catalog
        :param i: int type; the index of the book to retrieve
        :return: Book type; the book at index i of the catalog
        """
        try:
            start_time = time.time()
          
            # FIXME: Correct the line below
            book = self.bookCatalog.get(i)
            """FIXME: Replace this string with the correct code"""
          
            elapsed_time = time.time() - start_time
            print(f"Accessed the following book from catalog:{book}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)

    def searchBookByInfix(self, infix: str, k: int):
        """
        search the catalog for the first k books whose titles contain the given substring
        if less than k books contain the substring, then the max number of books that is
        less than k are displayed
        :param infix: str type; the substring that titles should contain
        :param k: int type; the max number of books to display
        """
        try:
            printed = 0
            n = self.bookCatalog.size()
            start_time = time.time()         
            # FIXME: Complete the implementation so that the first k books whose titles
            # contain the given infix are printed using the format
            # "-" * 25 + f"\nMatch found at catalog index {i}:\n{book}\n"
            for i in range(n):
                book = self.bookCatalog.get(i)
                if infix in book.title:
                    print("-" * 25 + f"\nMatch found at catalog index {i}:\n{book}\n")
                    printed += 1
                    if printed == k:
                        break
            elapsed_time = time.time() - start_time
            print(f"Found {printed} matches in {elapsed_time} seconds.")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)

    """ --------- METHODS RELATED TO THE SHOPPING CART --------- """
    def addBookByIndex(self, i: int):
        """
        adds the book at index i of the catalog into the shopping cart
        :param i: int type; the index in the catalog of the desired book
        """
        try:
            start_time = time.time()
            # FIXME: Correct the line below
            s = self.bookCatalog.get(i)
            """FIXME: Replace this string with the code that will 
            assign to s the book at index i of the catalog"""
            # FIXME: Add the book s to the shopping cart
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"\nAdded to shopping cart: {s} \nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)

    def removeFromShoppingCart(self):
        """
        removes and displays one book from the shopping cart in FIFO order
        """
        try:
            start_time = time.time()
            if self.shoppingCart.size() > 0:
                # FIXME: Correct the line below
                u = self.shoppingCart.remove()
                """FIXME: Replace this string with the code that will assign to u the book 
                that was removed from the shopping cart"""       
                elapsed_time = time.time() - start_time
                print(f"Removed from shopping cart the following book:\n{u}\nAction completed in {elapsed_time} seconds.")
            else:
                elapsed_time = time.time() - start_time
                print(f"Nothing to remove.  Shopping cart is empty.\nAction completed in {elapsed_time} seconds.")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)