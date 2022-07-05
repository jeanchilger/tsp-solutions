import time
import numpy as np
import math
from typing import Union
from ..solution import Solution
from util import graph_helper

class Christofides(Solution):
    def __init__(self):
        super(Christofides, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray, **kwargs: dict) -> np.ndarray:
        assert "timelimit" in kwargs

        timelimit = kwargs.pop("timelimit")

        return self._solve(adjacency_matrix, time.time(), timelimit)
    
    def _solve(
            self, adjacency_matrix: np.ndarray,
            start_time:int, timelimit: int) -> np.ndarray:
        best_path = None
        best_cost = math.inf

        graph_helper.compute_mst([1,2,3,4])

        while True:
            generated_path = np.array([np.random.randint(0, len(adjacency_matrix))])
            generated_cost = None

            visited = dict.fromkeys(range(len(adjacency_matrix)), False)
            visited[generated_path[0]] = True

            if time.time() - start_time > timelimit:
                break
            
        return best_path
    

