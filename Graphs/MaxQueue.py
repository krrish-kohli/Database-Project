from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        """
        constructor; initializes an empty MaxQueue
        """
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x: object):
        """
        adds a new element to the MaxQueue
        :param x: object type; the new element
        """
        SLLQueue.add(self, x)
        if self.max_deque.size() == 0:
            self.max_deque.add_first(x)
        else:
            max_ele = self.max_deque.get(0)
            #print("deque size:", n)
            if x > max_ele:
              self.max_deque.clear()
              self.max_deque.add_first(x)
            else:
                self.max_deque.add_last(x)
                p = self.max_deque.dummy.next
                for i in range(self.max_deque.n):
                  if p.x < x:
                    self.max_deque.remove(i)

    def remove(self) -> object:
        """
        removes and returns the element at the head of the MaxQueue
        :return: object type; the element that was removed from the head
        """
        r = SLLQueue.remove(self)
        if self.max_deque.size() != 0:
          if r == self.max_deque.get(0):
            self.max_deque.remove(0)
        return r

    def max(self):
        """
        returns the largest element currently stored in the MaxQueue
        :return: object type; the element with the largest value in the MaxQueue
        """
        p = self.max_deque.dummy.next
        max = self.max_deque.get(0)
        for i in range(self.max_deque.n):
          if p.x > max:
            max = p.x
          p = p.next
        return max
