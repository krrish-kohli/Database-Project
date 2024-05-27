from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty stack
        """
        self.n = 0
        self.head = None
        self.tail = None

    def push(self, x: object):
        """
        adds a new element to the head of the stack
        :param x: object type; the new element
        """
        u = self.Node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
          self.tail = u
        self.n += 1
        return x

    def pop(self) -> object:
        """
        removes and returns the element at the head of the stack
        :return: object type; the element that was removed from the stack
        :raises: IndexError if the stack is empty
        """
        if self.n == 0:
          raise IndexError()
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
          self.tail = None
        return x

    def size(self) -> int:
        """
        returns the number of elements in the stack
        :return: int type;
        """
        u = self.head
        count = 0
        while u != None:
          count += 1
          u = u.next
        return count

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
