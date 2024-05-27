class SortableBook:
  """
  Class: Book contains the details of the book. It allows comparing
  two instances according to their title.
  for example b1 < b2 if  b1.title < b2.title
  """

  def __init__(self, key, title, group, rank, similar):
      self.key = key
      self.title = title
      self.group = group
      self.rank = int(rank)
      self.similar = similar

  def __lt__(self, other):
      """
      This function allows to make direct comparison using the operator <
      between two Book objects based on their ranks
      """
      if isinstance(other, SortableBook):
          return self.title.lower() < other.title.lower()
      elif isinstance(other, str):
          return self.title.lower() < other.lower()
      else:
          raise TypeError(f"Operator < is not defined for object of type Book and {type(other)}")

  def __gt__(self, other):
      """
      This function allows to make direct comparison using the operator >
      between two Book objects based on their title
      """
      if isinstance(other, SortableBook):
          return self.title.lower() > other.title.lower()
      elif isinstance(other, str):
          return self.title.lower() > other.lower()
      else:
          raise TypeError(f"Operator > is not defined for object of type Book and {type(other)}")

  def __ge__(self, other):
      """
      This function allows to make direct comparison using the operator >=
      between two Book objects based on their title
      """
      if isinstance(other, SortableBook):
          return self.title.lower() >= other.title.lower()
      elif isinstance(other, str):
          return self.title.lower() >= other.lower()
      else:
          raise TypeError(f"Operator >= is not defined for object of type Book and {type(other)}")

  def __le__(self, other):
      """
      This function allows to make direct comparison using the operator <=
      between two Book objects based on their title
      """
      if isinstance(other, SortableBook):
          return self.title.lower() < other.title.lower()
      elif isinstance(other, str):
          return self.title.lower() < other.lower()
      else:
          raise TypeError(f"Operator < is not defined for object of type Book and {type(other)}")

  def __eq__(self, other):
      """
      This function allows for direct comparison using the operator ==
      between two Book objects based on their titles.  == is also supported betweeen Book and 'str'
      In such case, True is returned the title matches the given string
      """
      if isinstance(other, SortableBook):
          return self.title.lower() == other.title.lower()
      elif isinstance(other, str):
          return self.title.lower() == other.lower()
      else:
          raise TypeError(f"Operator == is not defined for object of type Book and {type(other)}")


  def __str__(self):
      """
      returns a string containing the book information
      """
      return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"

