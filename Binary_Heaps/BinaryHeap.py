import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
  """
    helper method; returns the index of the left child of the element at index i
    """
  return 2 * i + 1


def right(i: int) -> int:
  """
    helper method; returns the index of the right child of the element at index i
    """
  return 2 * (i + 1)


def parent(i: int) -> int:
  """
    helper method; returns the index of the parent of the element at index i
    """
  return (i - 1) // 2


def _new_array(n: int) -> np.array:
  """
    helper method; creates a new numpy array of 0's of size n
    """
  return np.zeros(n, object)


class BinaryHeap(Queue, Tree):

  def __init__(self):
    self.a = _new_array(1)
    self.n = 0

  def add(self, x: object):
    """
        adds a new element to the binary heap, ensuring that the
        heap invariant parent <= children is maintained
        :param x: object type; the new element
        :returns: boolean type; True if the element was successfully added
        """
    if len(self.a) == self.n:
      self._resize()
    self.a[self.n] = x
    self.n += 1
    self._bubble_up_last()

  def remove(self):
    """
        removes the smallest element from the heap and returns it
        :returns: object type;
        """
    if self.n == 0:
      raise IndexError("Heap is empty")
    x = self.a[0]
    self.a[0] = self.a[self.n - 1]
    self.n -= 1
    self._trickle_down_root()
    if 3 * self.n <= len(self.a):
      self._resize()
    return x

  def depth(self, u) -> int:
    """
        returns the depth of element u in the binary heap
        :returns: int type; the number of edges from the root to element u
        """
    bool = False
    i = 0
    for i in range(self.n):
      if self.a[i] == u:
        bool = True
        break
      i += 1
    if bool:
      return math.floor(math.log2(i+1))
    raise ValueError(u, " was not found.")


  def height(self) -> int:
    """
        returns the height of the tree
        :returns: int type
        """
    return math.floor(math.log2(self.n))

  def bf_order(self) -> list:
    """
        returns a list of the elements in the binary heap as they are traversed
        using Breadth-First order
        :returns: list type;
        """
    list = []
    for i in range(self.n):
      list.append(self.a[i])
    return list

  def in_order(self) -> list:
    """
        returns a list of the elements in the binary heap as they are traversed
        using in-order traversal
        :returns: list type;
        """
    indices = self._in_order(0)
    return [self.a[idx] for idx in indices]

  def post_order(self) -> list:
    """
        returns a list of the elements in the binary heap as they are traversed
        using post-order traversal
        :returns: list type;
        """
    indices = self._post_order(0)
    return [self.a[idx] for idx in indices]

  def pre_order(self) -> list:
    """
        returns a list of the elements in the binary heap as they are traversed
        using pre-order traversal
        :returns: list type;
        """
    indices = self._pre_order(0)
    return [self.a[idx] for idx in indices]

  def size(self) -> int:
    """
        returns the number of elements in the binary heap
        :returns: int type;
        """
    return self.n

  def get_min(self):
    """
        gets the smallest element in the binary heap without removing it
        :returns: object type;
        """
    return self.a[0]

  def _resize(self):
    """
        helper method; resizes the backing array to twice the
        number of elements, n, or 1 if n = 0.
        """
    a = _new_array(max(1, 2 * self.n))
    for i in range(self.n):
      a[i] = self.a[i]
    self.a = a

  def _bubble_up_last(self):
    """
        helper method to add(x); moves the latest added element
        of the heap to its correct position so that the invariant
        parent <= children is maintained.
        """
    i = self.n - 1
    p_idx = parent(i)
    while i > 0 and self.a[p_idx] > self.a[i]:
      temp = self.a[p_idx]
      self.a[p_idx] = self.a[i]
      self.a[i] = temp
      i = p_idx
      p_idx = parent(i)

  def _trickle_down_root(self):
    """
        helper method to remove(); moves the root of the heap to its correct
        position so that the invariant parent <= children is maintained.
        """
    i = 0
    l_idx = left(i)
    r_idx = right(i)
    while i < self.n and (l_idx < self.n or r_idx < self.n) and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
      min_idx = i
      if self.a[l_idx] < self.a[min_idx]:
        min_idx = l_idx

      if self.a[r_idx] < self.a[min_idx]:
        min_idx = r_idx

      temp = self.a[i]
      self.a[i] = self.a[min_idx]
      self.a[min_idx] = temp
      i = min_idx
      l_idx = left(i)
      r_idx = right(i)

  def _in_order(self, i):
    """
        helper method to in_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using in-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
    indices = []
    l_idx = left(i)
    r_idx = right(i)
    if 0 <= l_idx < self.n:
      indices.extend(self._in_order(l_idx))
    if 0 <= i < self.n:
      indices.append(i)
    if 0 <= r_idx < self.n:
      indices.extend(self._in_order(r_idx))
    return indices

  def _post_order(self, i):
    """
        helper method to post_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using post-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
    indices = []
    l_idx = left(i)
    r_idx = right(i)
    if 0 <= l_idx < self.n:
      indices.extend(self._post_order(l_idx))
    if 0 <= r_idx < self.n:
      indices.extend(self._post_order(r_idx))
    if 0 <= i < self.n:
      indices.append(i)
    return indices

  def _pre_order(self, i):
    """
        helper method to pre_order(); returns a list of the indices of 
        the elements in the subtree rooted at the element at index i as they are
        traversed using pre-order traversal
        :param i: int type; the index of the root of the subtree
        :returns: list type;
        """
    indices = []
    l_idx = left(i)
    r_idx = right(i)
    if 0 <= i < self.n:
      indices.append(i)
    if 0 <= l_idx < self.n:
      indices.extend(self._pre_order(l_idx))
    if 0 <= r_idx < self.n:
      indices.extend(self._pre_order(r_idx))

    return indices

  def __str__(self):
    """
        returns the string representation of the binary heap array
        :returns: str type;
        """
    return str(self.a[0:self.n])