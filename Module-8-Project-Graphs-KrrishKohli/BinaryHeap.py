import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    pass # FIXME: Replace with your implementation


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    pass # FIXME: Replace with your implementation


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    pass # FIXME: Replace with your implementation


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
        pass # FIXME: Replace with your implementation

    def remove(self):
        """
        removes the smallest element from the heap and returns it
        :returns: object type;
        """
        pass # FIXME: Replace with your implementation

    def depth(self, u) -> int:
        """
        returns the depth of element u in the binary heap
        :returns: int type; the number of edges from the root to element u
        """
        pass # FIXME: Replace with your implementation

    def height(self) -> int:
        """
        returns the height of the tree
        :returns: int type
        """
        pass # FIXME: Replace with your implementation

    def bf_order(self) -> list:
        """
        returns a list of the elements in the binary heap as they are traversed
        using Breadth-First order
        :returns: list type;
        """
        pass # FIXME: Replace with your implementation

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
        pass # FIXME: Replace with your implementation

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
        pass # FIXME: Replace with your implementation

    def _trickle_down_root(self):
        """
        helper method to remove(); moves the root of the heap to its correct
        position so that the invariant parent <= children is maintained.
        """
        pass # FIXME: Replace with your implementation


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
            pass # FIXME: Replace with your implementation
        if 0 <= i < self.n:
            indices.append(i)
        if 0 <= r_idx < self.n:
            pass # FIXME: Replace with your implementation
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
            pass # FIXME: Replace with your implementation
        if 0 <= r_idx < self.n:
            pass # FIXME: Replace with your implementation
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
            pass # FIXME: Replace with your implementation
        if 0 <= r_idx < self.n:
            pass # FIXME: Replace with your implementation
    
        return indices
    
    def __str__(self):
        """
        returns the string representation of the binary heap array
        :returns: str type;
        """
        return str(self.a[0:self.n])
    
    
    