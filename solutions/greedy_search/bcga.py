import time
import numpy as np
import math
from typing import Union
from ..solution import Solution

class BCGa(Solution):
    def __init__(self):
        super(BCGa, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        assert "timelimit" in kwargs

        timelimit = kwargs.pop("timelimit")

        return self._solve(adjacency_matrix, time.time(), timelimit)
    
    def _solve(
            self, adjacency_matrix: np.ndarray,
            start_time:int, timelimit: int) -> np.ndarray:
        best_path = None
        best_cost = math.inf

        while True:
            generated_path = np.array([np.random.randint(0, len(adjacency_matrix))])
            generated_cost = None

            visited = dict.fromkeys(range(len(adjacency_matrix)), False)
            visited[generated_path[0]] = True

            if time.time() - start_time > timelimit:
                break

            while len(generated_path) < len(adjacency_matrix):
                edge_index = 0

                indexes = []
                
                for i in range(0, len(adjacency_matrix)):
                    if not visited[i]:
                        indexes.append((i, adjacency_matrix[generated_path[-1]][i]))
                
                indexes = sorted(indexes, key=lambda x: x[1])

                edge_index = np.random.choice(
                        list(map(lambda x: x[0], indexes[:math.ceil(len(indexes) * 0.3)])))

                generated_path = np.append(generated_path, edge_index)
                visited[edge_index] = True
            
            generated_cost = self.evaluate(adjacency_matrix, generated_path)

            if generated_cost < best_cost:
                best_cost = generated_cost
                best_path = generated_path.copy()
        
        return best_path

