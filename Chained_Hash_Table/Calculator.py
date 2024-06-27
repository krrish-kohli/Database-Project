      import re
      import time
      import SLLStack
      import ChainedHashTable


      class Calculator:
          def __init__(self):
              self.dict = ChainedHashTable.ChainedHashTable()

          def balanced_parens(self, s: str) -> bool:
              """
              determines whether the given string contains balanced parentheses
              :param s: str type; the string to be checked
              :return: bool type; True if the string s contains balanced parentheses
              """
              stack = SLLStack.SLLStack()
              for c in s:
                  if c == "(":
                      stack.push(c)
                  elif c == ")":
                      if stack.size() == 0:
                          return False
                      else:
                          stack.pop()
              return stack.size() == 0

          def store_var(self, variable, value, replace=False):
              """
              stores the given mathematical variable and its corresponding value.
              If the variable already exists and should not be replaced, error message is printed and the variable is not stored.  Otherwise, the value of the existing variable is replaced with the new value.
              :param variable: str type;
              :param value: float type;
              :param replace: boolean type; if True, replaces the value of an existing variable; otherwise, prints an error message
              """
              start_time = time.time()

              added = self.dict.add(variable, value)

              elapsed_time = time.time() - start_time
              if added:
                  print(f"Stored {variable} = {value}.\nAction completed in {elapsed_time} seconds")
                  return True
              elif replace:
                  start_time = time.time()

                  old_val = self.dict.set(variable, value)

                  elapsed_time = time.time() - start_time
                  print(f"Replaced value {old_val} with {value}.\nAction completed in {elapsed_time} seconds.")
              else:
                  print(f"Variable {variable} is already stored with value {self.dict.find(variable)}.")
                  return False


          def print_stored_vars(self):
              """
              displays all math variables and their corresponding values stored
              on this instance of Calculator
              """
              start_time = time.time()
              keys = self.dict.get_keys()
              elapsed_time = time.time() - start_time
              for k in keys:
                  print(f"{k} = {self.dict.find(k)}")
              print(f"Displayed all stored keys with corresponding values.\nAction completed in {elapsed_time} seconds.")


          def print_expression(self, expression):
              """
              displays the given expression with variables replaced with their values
              stored on this instance of Calculator
              """
              variables = [x for x in re.split('\W+', expression) if x.isalnum()]
              everything_else = re.split('\w+', expression)
              start_time = time.time()
              for i in range(len(variables)):
                  var = variables[i]
                  val = self.dict.find(var)
                  if val is not None:
                      variables[i] = val
              i = 0
              j = 0
              while i < len(variables) and j < len(everything_else):
                  print(everything_else[j] + str(variables[i]), end="")
                  i += 1
                  j += 1
              while j < len(everything_else):
                  print(everything_else[j], end="")
                  j += 1
              while i < len(variables):
                  print(str(variables[i]), end="")
                  i += 1
              elapsed_time = time.time() - start_time
              print(f"\nPrinted expression with stored variables.\nAction completed in {elapsed_time} seconds.")