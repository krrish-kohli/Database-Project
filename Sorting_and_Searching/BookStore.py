import sys
import traceback
import time

import algorithms
import ArrayList
import DLList
import ChainedHashTable
from exceptions import InvalidStateException
import BinaryHeap
import BinarySearchTree
import BinaryTree
from Book import Book
import MaxQueue
from SortableBook import SortableBook


class BookStore:
    """
    Simulates a book system such as Amazon. It allows  searching,
    removing and adding to a shopping cart.  New items can be added to the
    catalog.  Existing items can be removed from the catalog
    """

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        self.mapKeysToIdxs = None
        self.mapTitlesToIdxs = None
        self.booksByRank = None
        self.catalogIsSorted = None

    """ --------- METHODS RELATED TO THE CATALOG --------- """

    def load_catalog(self, fileName: str, ds: str, sort_by: str):
        """
        reads the text file at the given directory and creates a list with all books.
        Each book record contains a key, title, group, rank (number of copies sold) and
        a list of keys of similar books
        :param fileName: str type; the name of the text file containing the book catalog
        :param ds: str type; the option of list data structure to use 1 - ArrayList, 2 - DLList
        :param sort_by: str type; the option of sorting algorithm to use:
                    1 - Quick-sort w/ random pivot, 3 - Quick-sort w/ first element pivot
                    If invalid option is given, catalog is not sorted
        """
        self.mapTitlesToIdxs = BinarySearchTree.BinarySearchTree()
        self.catalogIsSorted = False
        try:
            if ds == '1':
                self.bookCatalog = ArrayList.ArrayList()
                self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable(ArrayList.ArrayList)
            elif ds == '2':
                self.bookCatalog = DLList.DLList()
                self.mapKeysToIdxs = ChainedHashTable.ChainedHashTable()
            else:
                raise ValueError(f"Invalid option {ds} for data structure given")

            # begin loading catalog
            start_time = time.time()
            with open(fileName, encoding="utf8") as f:
                for line in f:
                    (key, title, group, rank, similar) = line.split("^")
                    s = SortableBook(key, title, group, rank, similar)
                    self.bookCatalog.append(s)

            # sorting catalog
            if sort_by == '1':
                algorithms.quick_sort(self.bookCatalog)
                self.catalogIsSorted = True

                print('\n' + '-' * 40)
                print("Sorted Catalog:")
                for i in range(self.bookCatalog.size()):
                    print(f"Index {i}: {self.bookCatalog.get(i).title}")

            elif sort_by == '2':
                algorithms.quick_sort(self.bookCatalog, False)
                self.catalogIsSorted = True

                print('\n' + '-' * 40)
                print("Sorted Catalog:")
                for i in range(self.bookCatalog.size()):
                    print(f"Index {i}: {self.bookCatalog.get(i).title}")
            else:
                print("Invalid sorting algorithm selected.  Catalog will not be sorted.")
            elapsed_time = time.time() - start_time

            # loading dictionaries
            for i in range(self.bookCatalog.size()):
                book = self.bookCatalog.get(i)
                # chained-hash table maps (book key, catalog idx)
                self.mapKeysToIdxs.add(book.key, i)
                # binary search tree maps (book title, catalog idx)
                self.mapTitlesToIdxs.add(book.title.lower(), i)
            print(f"Loaded {self.bookCatalog.size()} books in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def get_book_at_index(self, i: int):
        """
        retrieves the Book at index i of the catalog
        :param i: int type; the index of the book to retrieve
        :return: Book type; the book at index i of the catalog
        """
        try:
            start_time = time.time()
            book = self.bookCatalog.get(i)
            elapsed_time = time.time() - start_time
            print(f"Accessed the following book from catalog:{book}\nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_infix(self, infix: str, n: int, by_rank: bool):
        """
        search the catalog for the first n books whose titles contain the given substring
        if less than k books contain the substring, then the max number of books that is
        less than k are displayed
        :param infix: str type; the substring that titles should contain
        :param n: int type; the max number of books to display
        :param by_rank: bool type; if True, matching books are displayed in order
                        of highest rating; otherwise, matching books are displayed
                        in order of first match according usingby_rankp linear search
        """
        if not by_rank:
            try:
                printed = 0
                start_time = time.time()
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        print("-" * 25 + f"\nMatch found at catalog index {i}:\n{book}\n")
                        printed += 1
                    if printed == n:
                        break
                elapsed_time = time.time() - start_time
                print(f"Found {printed} matches in {elapsed_time} seconds.")
            except Exception:
                print("The following unexpected error occurred:")
                traceback.print_exc(limit=2, file=sys.stdout)
        else:
            try:

                start_time = time.time()
                self.booksByRank = BinaryHeap.BinaryHeap()
                for i in range(self.bookCatalog.size()):
                    book = self.bookCatalog.get(i)
                    if infix.lower() in book.title.lower():
                        b = Book(book.key, book.title, book.group, -1 * book.rank, book.group)
                        self.booksByRank.add(b)
                printed = 0
                for i in range(self.booksByRank.size()):
                    top_book = self.booksByRank.remove()
                    top_book.rank = abs(top_book.rank)
                    print("-" * 25 + f"\nTop Match #{printed + 1}:\n{top_book}\n")
                    printed += 1
                    if printed == n:
                        break
                elapsed_time = time.time() - start_time
                print(f"Found {printed} matches in {elapsed_time} seconds.")
            except Exception:
                print("The following unexpected error occurred:")
                traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_title(self, title: str, search_algo):
        """
        finds and displays the Book with the given title, if it exists
        :param title: str type; the title to search for
        :param search_algo: str type; the option of search algorithm to use:
                    1 - Linear search, 2 - Binary search
        """
        try:
            if search_algo == '1':
                start_time = time.time()

                # Perform linear search to determine 'idx'
                idx = None
                for i in range(self.bookCatalog.size()):
                    if self.bookCatalog.get(i).title.lower() == title.lower():
                        idx = i
                        break

                elapsed_time = time.time() - start_time
            elif search_algo == '2':
                if self.catalogIsSorted:
                    start_time = time.time()

                    # Perform binary search to determine 'idx'
                    left, right = 0, self.bookCatalog.size() - 1
                    while left <= right:
                        mid = (left + right) // 2
                        if self.bookCatalog.get(mid).title.lower() == title.lower():
                            idx = mid
                            break
                        elif self.bookCatalog.get(mid).title.lower() < title.lower():
                            left = mid + 1
                        else:
                            right = mid - 1
                    else:
                        idx = None

                    elapsed_time = time.time() - start_time
                else:
                    raise InvalidStateException("Cannot perform Binary Search on unsorted catalog.")
            else:
                raise ValueError("Invalid searching algorithm was selected.  Please try again.")
            if idx is None:
                print(f"\nThe title \"{title}\" does not exist in the catalog.")
            else:
                print(
                    "-" * 40 + f"\nThe following book matching the given title was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"Action completed in {elapsed_time} seconds.")

        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def search_by_key(self, key):
        """
        displays the book with the given key if it exists
        :param key: str type; the key of the book to search for
        """
        try:
            start_time = time.time()
            idx = self.mapKeysToIdxs.find(key)
            elapsed_time = time.time() - start_time
            if idx is None:
                print(f"\nThere is no book with key \"{key}\" in the catalog.")
            else:
                print(
                    f"\nThe following book matching the given key was found at catalog index {idx}:{self.bookCatalog.get(idx)}")
            print(f"Action completed in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)
        return

    def search_by_prefix(self, prefix, n):
        """
        displays the first n books in alphabetical order whose titles
        begin with the given prefix (ignores case).
        :param prefix: str type;
        :param n: int type; the max number of results to display
        """
        lowercase_prefix = prefix.lower()
        try:
            start_time = time.time()
            r = self.mapTitlesToIdxs.bookstore_helper(lowercase_prefix)

            if r is None:
                print(f"\nThere are no titles that begin with \"{prefix}\" in the catalog.")
            else:
                bt = BinaryTree.BinaryTree()
                bt.r = r
                
                nodes = bt.bf_order()
                nodes_array = ArrayList.ArrayList()
                for node in nodes:
                    nodes_array.append(node)
                printed = 0
                
                for i in range(len(nodes)):
                    idx = nodes[i].v
                    book = self.bookCatalog.get(idx)
                    if lowercase_prefix == book.title[0:len(prefix)].lower():
                        print('-' * 20 + f"\nMatch #{printed + 1} at index {idx}:\n{book}")
                        printed += 1
                    if n == printed:
                        break
            elapsed_time = time.time() - start_time
            print(f"\nFound {printed} matches in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)
        return

    """ --------- METHODS RELATED TO THE SHOPPING CART --------- """

    def add_book_at_index(self, i: int):
        """
        adds the book at index i of the catalog into the shopping cart
        :param i: int type; the index in the catalog of the desired book
        """
        try:
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"\nAdded to shopping cart: {s} \nAction completed in {elapsed_time} seconds.")
        except IndexError:
            print(f"Index {i} is out of bounds for catalog of size {self.bookCatalog.size()}")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def remove_from_shopping_cart(self):
        """
        removes and displays one book from the shopping cart in FIFO order
        """
        try:
            start_time = time.time()
            if self.shoppingCart.size() > 0:
                u = self.shoppingCart.remove()
                elapsed_time = time.time() - start_time
                print(
                    f"Removed from shopping cart the following book:\n{u}\nAction completed in {elapsed_time} seconds.")
            else:
                elapsed_time = time.time() - start_time
                print(f"Nothing to remove.  Shopping cart is empty.\nAction completed in {elapsed_time} seconds.")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)

    def cart_best_seller(self):
        """
        displays the item with the highest number of sales that is in
        the shopping cart
        """
        try:
            start_time = time.time()
            bestseller = self.shoppingCart.max()
            elapsed_time = time.time() - start_time
            print("All books in shopping cart:")
            for book in self.shoppingCart:
                print('-' * 10 + str(book))
            print('-' * 30 + f"\nThe highest ranking book:{bestseller}\nAction completed in {elapsed_time} seconds")
        except Exception as e:
            print("The following unexpected error occurred:")
            traceback.print_exc(limit=2, file=sys.stdout)