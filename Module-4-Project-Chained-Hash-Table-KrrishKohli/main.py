import Book
import Calculator
import BookStore
import tester

import time


def menu_calculator():
  calculator = Calculator.Calculator()
  option = ""
  while option.upper() != 'Q':
    menu = "-" * 40 + "\nCALCULATOR MENU\n1. Store variable values.\n2. Display stored variables.\n3. Print expression with stored values.\nQ. Return to main menu\n\nEnter your selection: "
    option = input(menu)
    if option == '1':
      r = ''
      while r.upper() != 'N':
        var = input("-" * 40 + "\nEnter the variable: ")
        value = float(input(f"Enter its value: {var} = "))
        added = calculator.store_var(var, value)
        if not added:
          s = input("Replace value? Y/N: ")
          if s.upper() == 'Y':
            calculator.store_var(var, value, True)
        r = input("\nEnter another variable? Y/N: ")
    elif option == '2':
      print("-" * 40 + f"\nDisplaying stored variables:")
      calculator.print_stored_vars()

    elif option == '3':
      expression = input("-" * 40 +
                         "\nIntroduce the mathematical expression: ")
      if calculator.balanced_parens(expression):
        print("Result:", end=" ")
        calculator.print_expression(expression)
      else:
        print(
            f"Parentheses are NOT BALANCED. Replacing values is not supported for invalid expressions.\n"
        )

    elif option.upper() != 'Q':
      print("Invalid selection.  Please try again.\n")


def menu_bookstore_system():
  bookStore = BookStore.BookStore()
  option = ''
  while option.upper() != 'Q':
    print("-" * 40 + """
        BOOKSTORE MENU
        1. Load book catalog
        2. Edit the book catalog
        3. Access book at index
        4. Search Menu
        5. Shopping Cart Menu
        Q. Return to main menu
        """)
    option = input("Enter your selection: ")
    if option == "1":
      file_name = input("-" * 40 + "\nIntroduce the name of the file: ")
      ds = input(
          "\nEnter the desired data structure option:\n\t1. ArrayList\n\t2. DLList\n\nYour selection: "
      )
      bookStore.loadCatalog(file_name, ds)
    elif option == "2":
      option2 = ''
      while option2.upper() != 'Q':
        print("-" * 40 + """
                EDIT CATALOG MENU
                1. Insert a book to the catalog
                2. Delete an existing book
                Q. Return to bookstore menu
                """)
        option2 = input("Enter your selection: ")
        if option2 == '1':
          key = input("-" * 40 + "\nEnter the book key: ")
          title = input("Enter the book title: ")
          group = input("Enter the book group: ")
          rank = input("Enter the book rank: ")
          similar = input("Input keys of similar books separated by a space: ")
          book = Book.Book(key, title, group, rank, similar)
          idx = int(input("Enter the index of insertion: "))
          bookStore.addToCatalog(idx, book)
        elif option2 == '2':
          i = int(
              input("-" * 40 +
                    "\nIntroduce the index to remove from catalog: "))
          bookStore.removeFromCatalog(i)
    elif option == "3":
      idx = int(input("-" * 40 + "\nIntroduce the index: "))
      bookStore.getBookAtIndex(idx)

    elif option == "4":
      s = ''
      while s.upper() != 'Q':
        print("-" * 40 + """
                    SEARCH MENU
                    1. Search for matching infix
                    2. Search for matching title
                    3. Search for matching key
                    Q. Return to bookstore menu
                            """)
        s = input("Enter your selection: ")
        if s == '1':
          infix = input("-" * 40 + "\nIntroduce the query to search for: ")
          cnt = int(input("Enter max number of results: "))
          bookStore.searchBookByInfix(infix, cnt)
        elif s == '2':
          title = input("-" * 40 + "\nIntroduce the title to search for: ")
          bookStore.idxOfTitle(title)
        elif s == '3':
          key = input("-" * 40 + "\nIntroduce the book key to search for: ")
          bookStore.searchByKey(key)
        elif s.upper() != 'Q':
          print("Invalid selection.  Please try again.")

    elif option == "5":
      s = ''
      while s.upper() != 'Q':
        print("-" * 40 + """
                SHOPPING CART MENU
                1. Add a book by index to shopping cart
                2. Remove from the shopping cart
                3. Get the cart bestseller
                Q. Return to bookstore menu
                """)
        s = input("Enter your selection: ")
        if s == '1':
          i = int(
              input("-" * 40 +
                    "\nIntroduce the index to add to shopping cart: "))
          bookStore.addBookByIndex(i)
        elif s == '2':
          print("-" * 40)
          bookStore.removeFromShoppingCart()
        elif s == '3':
          print("-" * 40)
          bookStore.cartBestSeller()
        elif s != 'q':
          print("Invalid selection.  Please try again.")

    elif option.upper() != 'Q':
      print("Invalid selection.  Please try again.\n")


# main: Create the main menu
def main():
  option = ""
  while option.upper() != 'Q':
    print("-" * 40 + """
        MAIN MENU
        1. Calculator
        2. Bookstore System
        3. Run your own tester
        Q. Quit
        """)
    option = input("Enter your selection: ")

    if option == "1":
      menu_calculator()
    elif option == "2":
      menu_bookstore_system()
    elif option == "3":
      print("\n" + "-" * 40)
      tester.test()
    elif option.upper() != 'Q':
      print("Invalid selection.  Please try again.\n")


if __name__ == "__main__":
  main()
