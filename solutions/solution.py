import numpy as np
import time
from abc import ABC, abstractmethod


class Solution(ABC):
    def __init__(self):
        self.exec_time = None
        super(Solution, self).__init__()

    @abstractmethod
    def solve(self, adjacency_matrix: np.ndarray) -> np.ndarray:
        pass

    def __call__(self, adjacency_matrix: np.ndarray) -> None:
        start_time = time.time()
        path = self.solve(adjacency_matrix)
        self.exec_time = time.time() - start_time

        return path