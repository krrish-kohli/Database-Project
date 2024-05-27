  import sys
  import traceback

  from Book import Book
  import ArrayList
  import MaxQueue
  import time
  import DLList
  import ChainedHashTable


  class BookStore:
      """
      Simulates a book system such as Amazon. It allows  searching,
      removing and adding to a shopping cart.  New items can be added to the
      catalog.  Existing items can be removed from the catalog
      """

      def __init__(self):
          self.bookCatalog = None
          self.shoppingCart = MaxQueue.MaxQueue()
          self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable()

      """ --------- METHODS RELATED TO THE CATALOG --------- """
      def loadCatalog(self, fileName: str, ds: str):
          """
          reads the text file at the given directory and creates a list with all books.
          Each book record contains a key, title, group, rank 
          (number of copies sold) anda list of keys of similar books
          :param fileName: str type; the name of the text file containing 
          the book catalog
          :param ds: str type; the option of list data structure to use 
          1 - ArrayList, 2 - DLList
          """
          try:
              if ds == '1':
                  self.bookCatalog = ArrayList.ArrayList()
              elif ds == '2':
                  self.bookCatalog = DLList.DLList()
              else:
                  raise ValueError(f"Invalid option {ds} for data structure given")
              with open(fileName, encoding="utf8") as f:
                  # The following line is the time that the computation starts
                  start_time = time.time()
                  for line in f:
                      (key, title, group, rank, similar) = line.split("^")
                      s = Book(key, title, group, rank, similar)
                      self.bookCatalog.append(s)
                      idx = self.bookCatalog.size() - 1
                      self.mapKeysToIdxs.add(key, idx) # mapping the key to the index of the book in the catalog
                  elapsed_time = time.time() - start_time
                  print(f"Loaded {self.bookCatalog.size()} books in {elapsed_time} seconds.")
          except Exception as e:
              print("The following unexpected error occurred:")
              traceback.print_exc(limit=2, file=sys.stdout)


      def addToCatalog(self, i, book : Book):
          """
          inserts a new book to the catalog at the given index
          :param i: int type; the index of insertion
          :param book: Book type; the new book
          :return: None
          """
          try:
            print(f"Current catalog size: {self.bookCatalog.size()}")
            start_time = time.time()
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
              removed_book = self.bookCatalog.remove(i)  
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

      def idxOfTitle(self, title: str):
        """
        finds the index of the Book with the given title if it exists
        :param title: str type; gets the catalog index of the Book with
                      the given title if it exists; None otherwise
        """
        try:
            start_time = time.time()
            idx = self.bookCatalog.index_of(title)
            "FIXME: Replace this string with the correct code"
            elapsed_time = time.time() - start_time
            if idx is None:
                print(f"\nThe title \"{title}\" does not exist in the catalog.")
            else:
                print(f"\nThe following book matching the given title was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"Action completed in {elapsed_time} seconds.")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:\n", e)


      def searchByKey(self, key):
        """
        displays the book with the given key if it exists
        :param key: str type; the key of the book to search for
        """
        try:
            start_time = time.time()

            # FIXME: 'idx' should be the index of the book with the given key
            #       HINT: Use the mapKeysToIdxs data structure
            idx = self.mapKeysToIdxs.find(key) # FIXME: Replace this with the correct method call
            "FIXME: Replace this string with the correct code"
            elapsed_time = time.time() - start_time
            if idx is None:
                print(f"\nThere is no book with key \"{key}\" in the catalog.")
            else:
                print(
                    f"\nThe following book matching the given key was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"Action completed in {elapsed_time} seconds.")
        except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

      """ --------- METHODS RELATED TO THE SHOPPING CART --------- """
      def addBookByIndex(self, i: int):
          """
          adds the book at index i of the catalog into the shopping cart
          :param i: int type; the index in the catalog of the desired book
          """
          try:
              start_time = time.time()
              s = self.bookCatalog.get(i)
              """FIXME: Replace this string with the code that will 
              assign to s the book at index i of the catalog"""
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

      def cartBestSeller(self):
          try:
            start_time = time.time()
            max_rank = 0
            for book in self.shoppingCart:
              if book.rank > max_rank:
                max_rank = book.rank
                bestseller = book
            "FIXME: Replace this string with the code that will assign to bestseller the Book object with the highest rank in the shopping cart"
            elapsed_time = time.time() - start_time
            print("All books in shopping cart:")
            for book in self.shoppingCart:
                print('-'*10 + str(book))
            print('-'*30 +f"\nThe highest ranking book:{bestseller}\nAction completed in {elapsed_time} seconds")
          except AttributeError as e:
            print("The following unexpected error occurred:\n", e)
            print("\nCHECK: Did you load the catalog?")
          except Exception as e:
            print("The following unexpected error occurred:\n", e)
