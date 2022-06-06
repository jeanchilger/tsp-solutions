import numpy as np
import time
from abc import ABC, abstractmethod

from util import graph_helper


class Solution(ABC):
    def __init__(self):
        self.exec_time = None
        super(Solution, self).__init__()

    @abstractmethod
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        pass

    def evaluate(self, adjacency_matrix: np.ndarray, path: np.ndarray) -> float:
        """
        Evaluates the quality of the solution. In fact, computes
        the distance to traverse the graph using `path`.
        The lower the output the better.

        Args:
            adjacency_matrix (np.ndarray): Adjacency matrix
                representing the graph.
            path (np.ndarray): Path representing the solution.

        Returns:
            float: The distance to traverse the graph.
        """

        return graph_helper.compute_path_cost(adjacency_matrix, path)

    def __call__(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> None:
        start_time = time.time()
        path = self.solve(adjacency_matrix, **kwargs)
        self.exec_time = time.time() - start_time

        return path
