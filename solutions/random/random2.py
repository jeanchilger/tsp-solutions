from math import inf
import time
import numpy as np
from ..solution import Solution


class Random2(Solution):
    def __init__(self):
        super(Random2, self).__init__()
    
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
        first_node = np.random.randint(len(adjacency_matrix))
        
        visited = np.zeros(len(adjacency_matrix), dtype=bool)

        return np.concatenate([
            [first_node],
            self._traverse(first_node, adjacency_matrix, visited)
        ])   

    def _traverse(
            self, node: int, adjacency_matrix: np.ndarray,
            visited: np.ndarray) -> np.ndarray:
        """
        Recursively traverses the graph represented by the given adjacency
        matrix in a random fashion.

        The next node will be a not visited node that has a
        direct connection with the current node.

        To close a full cycle, the returned path must be further
        concatenated with the first node.

        Args:
            node (int): Current node being visited.
            adjacency_matrix (np.ndarray): Representation of the graph.
            visited (np.ndarray): Array of visited nodes.

        Returns:
            np.ndarray: The path traversed.
        """

        visited[node] = True

        if len(np.where(visited == False)[0]) == 0:
            return np.array([node])

        next_node = np.random.choice(
                np.intersect1d(
                        np.where(visited == False)[0],
                        np.where(adjacency_matrix[node] != 0)[0]))

        return np.concatenate([
            self._traverse(next_node, adjacency_matrix, visited),
            [node]])
