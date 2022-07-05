import unittest
import numpy as np
from util import graph_helper

class TestGraphHelper(unittest.TestCase):
    def setUp(self):
        self.adjacencyMatrixKruskal = self._make_kruskal_graph()
        self.mstKruskal = self._make_kruskal_expected_mst()

    def test_kruskal(self):
        # Tests for the example in https://en.wikipedia.org/wiki/Kruskal%27s_algorithm#Example
        mst = graph_helper.compute_mst(self.adjacencyMatrixKruskal)

        for edge in mst:
            self.assertIn((edge[0], edge[1]), self.mstKruskal)

    def _make_kruskal_graph(self):
        graph = np.zeros((7, 7))
        graph[0][1] = graph[1][0] = 7
        graph[0][3] = graph[3][0] = 5
        graph[1][2] = graph[2][1] = 8
        graph[1][3] = graph[3][1] = 9
        graph[1][4] = graph[4][1] = 7
        graph[2][4] = graph[4][2] = 5
        graph[3][4] = graph[4][3] = 15
        graph[3][5] = graph[5][3] = 6
        graph[4][5] = graph[5][4] = 8
        graph[4][6] = graph[6][4] = 9
        graph[5][6] = graph[6][5] = 11

        return graph

    def _make_kruskal_expected_mst(self):
        edge_list = [
            (0, 3),
            (3, 0),
            (2, 4),
            (4, 2),
            (3, 5),
            (5, 3),
            (0, 1),
            (1, 0),
            (1, 4),
            (4, 1),
            (4, 6),
            (6, 4),
        ]

        return edge_list
