from pprint import pprint
from typing import Any
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


def compute_mst(adjacency_matrix: np.ndarray) -> np.ndarray:
    """
    Computes the minimum spanning tree for 
    the graph representated by adjacency_matrix, using
    Kruskal's algorithm.

    Args:
        adjacency_matrix (np.ndarray): Adjacency matrix
            representation of graph

    Returns:
        np.ndarray: Minimum spanning tree.
    """

    ds_parent = [None] * len(adjacency_matrix)
    ds_size = [None] * len(adjacency_matrix)

    mst = []

    edge_list = []
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] > 0:
                edge_list.append((i, j, adjacency_matrix[i][j]))
    
    edge_list = sorted(edge_list, key=lambda x: x[2])

    for i in range(len(adjacency_matrix)):
        _disjoint_set_make_set(ds_parent, ds_size, i)

    for edge in edge_list:
        if (_disjoint_set_find(ds_parent, edge[0]) != 
                _disjoint_set_find(ds_parent, edge[1])):
            mst.append(edge)
            _disjoint_set_union(ds_parent, ds_size, edge[0], edge[1])

    return mst


# Disjoint Set function
def _disjoint_set_make_set(parent: list, size: list, x: int) -> None:
    """
    Creates a new disjoint set for the given element x.

    Args:
        parent (list): List of parents for disjoint set.
        size (list): List of sizes of sets.
        x (int): Element to be created.
    """

    parent[x] = x
    size[x] = 1


def _disjoint_set_find(parent: list, x: int) -> int:
    """
    Returns the parent (set representative) of the given
    element. Uses path halving.

    Args:
        parent (list): List of parents for disjoint set.
        x (int): Element to get the parent of.

    Returns:
        int: The parent of x.
    """

    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return parent[x]


def _disjoint_set_union(parent: list, size: list, x: int, y: int) -> None:
    """
    Unites the elements x and y into a single set.

    Args:
        parent (list): List of parents for disjoint set.
        size (list): List of sizes of sets.
        x (int): Element to be united.
        y (int): Element to be united.
    """

    x_root = _disjoint_set_find(parent, x)
    y_root = _disjoint_set_find(parent, y)

    if x_root == y_root:
        return

    if size[x_root] > size[y_root]:
        parent[y_root] = x_root
        size[x_root] += size[y_root]
    
    else:
        parent[x_root] = y_root
        size[y_root] += size[x_root]


def find_maximum_matching(adjacency_matrix: np.ndarray) -> np.ndarray:
    matching = np.zeros(adjacency_matrix.shape)

    augmenting_path = _find_augmenting_path(adjacency_matrix, matching)
    # if augmenting_path is not empty add it fo matching, and compute again
    # else return  matching


def _find_augmenting_path(
        adjacency_matrix: np.ndarray, matching: np.ndarray) -> np.ndarray:

    # compute blossoms
    # contract blossoms
    return matching
