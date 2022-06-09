from pprint import pprint
import tsplib95
import numpy as np

def make_adjacency_matrix(problem: tsplib95.models.StandardProblem) -> np.ndarray:
    """
    Returns the adjacency matrix that represents the graph
    provided by the coordinates of the cities defined in `problem`.

    Any point M[i][j] in the adjacency matrix M represents the distance between
    city i to city j, rounded to the nearest integer.

    Args:
        problem (tsplib95.models.StandardProblem): A problem instance from file.

    Returns:
        np.ndarray: The adjacency matrix.
    """

    coords = problem.node_coords

    mtrx = np.zeros((len(coords), len(coords)))

    for edge_src in coords.keys():
        for edge_dst in coords.keys():
            src = np.asarray(coords[edge_src])
            dst = np.asarray(coords[edge_dst])

            mtrx[edge_src - 1, edge_dst - 1] = round(np.linalg.norm(src - dst))

    return mtrx


def compute_path_cost(adjacency_matrix: np.ndarray, path: np.ndarray) -> int:
    """
    Returns the cost of traversing the graph defined by
    `adjacency_matrix` useing the given `path`.

    Args:
        adjacency_matrix (np.ndarray): Representation of the graph.
        path (np.ndarray): Path to be computed.

    Returns:
        int: The cost of the path.
    """

    cost = 0

    if len(path) == len(adjacency_matrix):
        path = np.concatenate([path, [path[0]]])

    for i in range(1, len(path)):
        cost += adjacency_matrix[path[i - 1], path[i]]
    
    return cost
