import time
from matplotlib import use
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

        while True:
            generated_path = np.array([np.random.randint(0, len(adjacency_matrix))])
            generated_cost = None

            visited = dict.fromkeys(range(len(adjacency_matrix)), False)
            visited[generated_path[0]] = True

            if time.time() - start_time > timelimit:
                break

            # 1. Compute Minimum Spanning Tree for the graph
            mst = graph_helper.compute_mst(adjacency_matrix)
            
            # 2. Get vertexes with odd degree
            vertex_degrees = np.zeros(len(adjacency_matrix))

            for src, dst, _ in mst:
                vertex_degrees[src] += 1
                vertex_degrees[dst] += 1

            vertex_degrees = np.array(
                    list(map(lambda x: x if x % 2 else -1, vertex_degrees)))

            # 3. Build an induced subgraph from the selected vertexes
            use_indexes = np.argwhere(vertex_degrees > -1).flatten()
            induced_subgraph = np.zeros((len(use_indexes), len(use_indexes)))

            for i in range(len(use_indexes)):
                for j in range(i + 1, len(use_indexes)):
                    induced_subgraph[i][j] = induced_subgraph[j][i] = adjacency_matrix[use_indexes[i]][use_indexes[j]]

            # 4. Find the perfect matching of the induced subgraph

            # 5. Connect edges in matching and MST to form a multigraph

            # 6. Form a Eulerian circuit in the multigraph

            # 7. Turn that circuit into a Hamiltonian cricuit
            
            

        return best_path
    

