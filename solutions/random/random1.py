from math import inf
import time
import numpy as np
from ..solution import Solution


class Random1(Solution):
    def __init__(self):
        super(Random1, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        assert "timelimit" in kwargs

        timelimit = kwargs.pop("timelimit")

        elapsed_time = 0
        start_time = time.time()
        best_solution = None
        best_solution_cost = inf

        while elapsed_time < timelimit:
            solution = self._solve(adjacency_matrix)
            solution_cost = self.evaluate(adjacency_matrix, solution)

            if solution_cost < best_solution_cost:
                best_solution = solution
                best_solution_cost = solution_cost
            
            elapsed_time = time.time() - start_time
        
        return best_solution
    
    def _solve(self, adjacency_matrix: np.ndarray) -> np.ndarray:
        all_nodes = np.arange(len(adjacency_matrix))

        np.random.shuffle(all_nodes)

        return np.concatenate([all_nodes, [all_nodes[0]]])