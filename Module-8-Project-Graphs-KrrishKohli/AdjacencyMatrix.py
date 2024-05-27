from Interfaces import Graph, List
from ArrayList import ArrayList
from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
import numpy as np


class AdjacencyMatrix(Graph):

    def __init__(self, n: int, dtype=ArrayList):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)
        self.dtype = dtype

    def add_edge(self, i: int, j: int):
        """
        adds a directed edge from node i to node j
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        """
        if i < 0 or i > self.n or j < 0 or j > self.n:
          raise IndexError()
        self.adj[i][j] = True

    def remove_edge(self, i: int, j: int):
        """
        removes the directed edge from node i to node j,
        if it exists in the graph.  Returns true if
        edge was removed, false otherwise
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) was removed, false otherwise.
        """
        if self.adj[i][j]:
          self.adj[i][j] = False
          return True
        else:
          return False

    def has_edge(self, i: int, j: int) -> bool:
        """
        determines if the directed edge from node i to node j
        exists in the graph.  Returns true if edge (i, j) exists,
        false otherwise.
        :param i: int type; index of node i
        :param j: int type; index of node j
        :raises: IndexError if i < 0 or j < 0
                 or i >= number of nodes or j >= number of nodes
        :returns: bool type; true if the edge (i, j) exists, false otherwise.
        """
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        """
        returns a List of node indices that are targets
        of the node at index i, i.e., a List of all nodes j
        such that (i, j) is an edge in the graph
        :param i: int type; index of source node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        list = ArrayList()
        for j in range(self.n):
          if self.has_edge(i, j):
            list.append(j)
        return list

    def in_edges(self, j) -> List:
        """
        returns a List of node indices that are sources
        of the node at index j, i.e., a List of all nodes i
        such that (i, j) is an edge in the graph
        :param j: int type; index of targe node
        :raises: IndexError if i < 0 or i >= number of nodes
        :returns: List subclass type; either an ArrayList or DLList
                  as specified by the attribute 'dtype'
        """
        edges = ArrayList()
        for i in range(self.n):
          if self.has_edge(i, j):
            edges.append(i)
        return edges

    def bfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Breadth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                  the attribute 'dtype'
        """
        traversal = []
        seen = [False] * self.n
        q = ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while len(q) != 0:
          i = q.remove()
          z = self.out_edges(i)

          for t in z:
            if not seen[t]:
              traversal.append(t)
              seen[t] = True
              q.add(t)
        return traversal

    def dfs(self, r: int):
        """
        returns a List of the node indices of the graph as they are
        traversed using Depth-First Search Traversal beginning at
        the node at index r
        :param r: int type; the index of the source node
        :returns: List subclass type; ArrayList or DLList as specified by
                  the attribute 'dtype'
        """
        traversal = []
        s = ArrayStack()
        seen = [False] * self.n
        s.push(r)
        while len(s) != 0:
          i = s.pop()
          if not seen[i]:
            traversal.append(i)
            seen[i] = True
            z = self.out_edges(i)
            for t in reversed(z):
              s.push(t)
        return traversal

    def size(self):
        """
        returns the number of nodes in the graph
        :returns: int type;
        """
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += f"{i}:  {self.adj[i]}\n"
        return s

