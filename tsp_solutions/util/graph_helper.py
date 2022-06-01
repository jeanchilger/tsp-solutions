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

    for edge_src in range(len(coords)):
        for edge_dst in range(len(coords)):
            src = np.asarray(coords[edge_src])
            dst = np.asarray(coords[edge_dst])

            mtrx[edge_src, edge_dst] = round(np.linalg.norm(src - dst))

    return mtrx
