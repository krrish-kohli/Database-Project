from Interfaces import Graph, List
import numpy as np
from ArrayList import ArrayList
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


class AdjacencyList(Graph):
      def __init__(self, n: int, dtype=ArrayList):
          self.n = n
          self.dtype = dtype
          self.adj = np.zeros(n, dtype=self.dtype)
          for i in range(self.n):
              self.adj[i] = self.dtype()

      def add_edge(self, i: int, j: int):
          """
          adds a directed edge from node i to node j
          :param i: int type; index of node i
          :param j: int type; index of node j
          :raises: IndexError if i < 0 or j < 0
                   or i >= number of nodes or j >= number of nodes
          """
          if i < 0 or i >= self.n or j < 0 or j >= self.n:
                raise IndexError()
          if j not in self.adj[i]:
                self.adj[i].append(j)

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
          if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError()
          for l in range(len(self.adj[i])):
            if self.adj[i].get(l) == j:
              self.adj[i].remove(l)
              return True
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
          for l in range(len(self.adj[i])):
            if self.adj[i].get(l) == j:
              return True
          return False

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
          if i < 0 or i > self.n:
            raise IndexError()
          return self.adj[i]

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
          if j < 0 or j > self.n:
            raise IndexError()
          incoming = ArrayList()
          for i in range(self.n):
            if self.has_edge(i, j):
              incoming.append(i)
          return incoming

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
            current = q.remove()
            neighbors = self.out_edges(current)

            for neighbor in neighbors:
                if not seen[neighbor]:
                    traversal.append(neighbor)
                    seen[neighbor] = True
                    q.add(neighbor)
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
              neighbors = self.out_edges(i)
              for neighbor in reversed(neighbors):
                s.push(neighbor)
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