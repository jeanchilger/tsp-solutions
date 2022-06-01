from pprint import pprint
import numpy as np

from util import graph_helper
from .solution import Solution
from math import inf


class BruteForce(Solution):
    def __init__(self):
        super(BruteForce, self).__init__()

    def solve(self, adjacency_matrix: np.ndarray) -> np.ndarray:
        unvisited = list(range(len(adjacency_matrix)))
        visited = []

        return self._traverse(adjacency_matrix, visited, unvisited)

    def _traverse(
            self, adjacency_matrix: np.ndarray,
            visited: np.ndarray, unvisited: np.ndarray) -> list:
        """
        Recursively traverses the graph represented by the given adjacency
        matrix, passing through all possible paths.

        Args:
            node (int): Current node being visited.
            adjacency_matrix (np.ndarray): Representation of the graph.
            visited (np.ndarray): Array of visited nodes.

        Returns:
            np.ndarray: The path traversed.
        """

        cost = (
            graph_helper.compute_path_cost(adjacency_matrix, visited)
            if len(unvisited) == 0
            else inf
        )

        for node in unvisited:
            visited.append(node)
            unvisited.remove(node)
            
            cost = min(cost, self._traverse(adjacency_matrix, visited, unvisited))

            unvisited.append(node)
            visited.remove(node)

        return cost
