from Interfaces import Queue


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty SLLQueue
        """
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        """
        adds an element to the tail of the queue
        :param x: object type; the new element
        """
        u = self.Node(x)
        if self.n == 0:
          self.head = u
        else:
          self.tail.next = u
        self.tail = u
        self.n += 1

    def remove(self) -> object:
        """
        removes and returns the head of the queue
        :return: object type; the element that was removed from the head of the queue
        :raises: IndexError if the queue is empty
        """
        if self.n == 0:
          raise IndexError()
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
          self.tail = None
        return x

    def reverse(self):
        """
        reverses the order of the queue
        """
        current_node = self.head
        previous = None
        next = None
        while current_node is not None:
          next = current_node.next
          current_node.next = previous
          previous = current_node
          current_node = next
        self.head = previous

    def size(self) -> int:
        """
        returns the number of elements in the queue
        :return: int type
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
