import time
import numpy as np
from math import inf
from typing import Union
from ..solution import Solution

class BTsh(Solution):
    def __init__(self):
        super(BTsh, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        assert "timelimit" in kwargs

        timelimit = kwargs.pop("timelimit")

        initial_path = np.arange(len(adjacency_matrix))

        np.random.shuffle(initial_path)

        return self._solve(
                initial_path, adjacency_matrix,
                time.time(), timelimit)
    
    def _solve(
            self, initial_path: np.ndarray,
            adjacency_matrix: np.ndarray,
            start_time:int, timelimit: int) -> np.ndarray:
        pass
    