import time
import numpy as np
from math import inf
from typing import Union
from ..solution import Solution

class BLPMsh(Solution):
    def __init__(self):
        super(BLPMsh, self).__init__()
    
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
        current_path = initial_path.copy()
        current_cost = self.evaluate(adjacency_matrix, initial_path)

        generated_path = initial_path.copy()
        generated_cost = None

        for i in range(1, len(adjacency_matrix)):
            for j in range(1, len(adjacency_matrix)):
                
                if time.time() - start_time > timelimit:
                    break

                if i != j:
                    # shifts j into i
                    jth = current_path[j]
                    generated_path = np.concatenate([
                        self._get_list(current_path[:j]),
                        self._get_list(current_path[j + 1:]),
                    ])

                    generated_path = np.insert(generated_path, i, jth)

                    # conputes quality of generated_path
                    generated_cost = self.evaluate(
                            adjacency_matrix, generated_path)

                    if generated_cost < current_cost:
                        return self._solve(
                                generated_path, adjacency_matrix,
                                start_time, timelimit)

        return generated_path
    
    def _get_list(self, array: np.ndarray) -> Union[list, np.ndarray]:
        return array if isinstance(array, np.ndarray) else [array]