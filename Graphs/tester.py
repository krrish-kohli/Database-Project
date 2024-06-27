from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix
import random
import copy



def test():
        """write your own tester in this function"""
        n = 4
        edges = [(random.randint(0, n-1), random.randint(0, n-1)) for i in range(6)]
        graph_list = AdjacencyList(n)
        graph_matrix = AdjacencyMatrix(n)
        for edge in edges:
            i = edge[0]
            j = edge[1]
            graph_list.add_edge(i, j)
            graph_matrix.add_edge(i, j)
        print("Edges:", edges)
        print("Adjacency list graph:\n", graph_list)
        print("Adjacency matrix graph:\n", graph_matrix)
        