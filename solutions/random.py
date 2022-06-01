import numpy as np
from .solution import Solution


class Random(Solution):
    def __init__(self):
        super(Random, self).__init__()
    
    def solve(self, adjacency_matrix: np.ndarray) -> np.ndarray:
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
