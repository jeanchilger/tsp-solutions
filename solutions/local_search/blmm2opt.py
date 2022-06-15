import time
import numpy as np
from math import inf
from typing import Union
from ..solution import Solution

class BLMM2opt(Solution):
    def __init__(self):
        super(BLMM2opt, self).__init__()
    
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

        while True:
            initial_cost = current_cost

            for i in range(1, len(adjacency_matrix) - 1):
                for j in range(i + 1, len(adjacency_matrix)):
                    
                    if time.time() - start_time > timelimit:
                        break

                    generated_path = np.concatenate([
                        current_path[:i],
                        np.flip(current_path[i:j + 1]),
                        current_path[j + 1:],
                    ])

                    generated_cost = self.evaluate(
                            adjacency_matrix, generated_path)

                    if generated_cost < current_cost:
                        current_path = generated_path.copy()
                        current_cost = generated_cost
                else:
                    continue
                break
            
            if initial_cost == current_cost:
                break

        return generated_path