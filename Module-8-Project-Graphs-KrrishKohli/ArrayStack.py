import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    """
        ArrayStack: Implementation of the Stack interface based on Arrays.
        All the @abstractemthods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple,
        s = ArrayStack()
        print(s)
        print(len(s))
    """

    def __init__(self):
        self.n = 0
        self.a = np.zeros(self.n, dtype=object)  # this is numpy array

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, dtype=object)

    def resize(self):
        """
        resizes the array to twice the number of existing elements
        or 1 if no elements exist.  Existing elements are copied in LIFO order.
        """
        b = self.new_array(max(1, 2 * self.n))
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b

    def get(self, i: int) -> object:
        """
        gets the element at index i of the LIFO stack
        :param i: int type; the index of the element to
        :return:
        """
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        return self.a[i]

    def set(self, i: int, x: object) -> object:
        """
        sets the value of index i to value x
        :param i: int type; the integer index that is non-negative but less than the number of elements
        :param x: object type; the new value to be placed at index i
        :return: object type; the old value that was replaced from index i
        """
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        temp = self.a[i]
        self.a[i] = x
        return temp

    def add(self, i: int, x: object):
        """
        inserts element x at index i by shifting all elements at indices j > i
        one position to the right
        :param i: int type; the integer index where the element will be inserted
        :param x: object type; the element to be inserted
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > self.n:
          raise IndexError()
        if len(self.a) == self.n:
          self.resize()
        for k in range(self.n, i, -1):
          self.a[k] = self.a[k - 1]
        self.a[i] = x
        self.n += 1
        return True

    def remove(self, i: int) -> object:
        """
        removes the element at index i by shift all elements at indices j > i
        one position to the left
        :param i: int type; the integer index of the element to be removed
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        else:
            y = self.a[i]
            self.a[i: self.n - 1] = self.a[i + 1: self.n]
            self.n -= 1
            if len(self.a) >= 3 * self.n:
                self.resize()
            return y

    def push(self, x: object):
        """
        adds a given element to the stack in LIFO order
        :param x: object; the element to be added
        :return: None
        """
        self.add(self.n, x)

    def pop(self) -> object:
        """
        removes the head of the LIFO stack
        :return: object; the element at the head of the stack
        """
        return self.remove(self.n - 1)

    def size(self):
        """
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        """
        return self.n

    def __contains__(self, item):
        return item in self.a

    def __str__(self) -> str:
        """
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        """
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
