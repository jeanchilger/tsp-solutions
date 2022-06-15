import numpy as np
import tsplib95


def load_problem(fname: str) -> tsplib95.models.StandardProblem:
    """
    Loads the problems from file, and returns
    a list with them.

    Args:
        fname (str): _description_

    Returns:
        tsplib95.models.StandardProblem: _description_
    """

    return tsplib95.load('data/{}.tsp'.format(fname))


def load_adjacency_matrix(fname: str) -> np.ndarray:
    """
    Loads a adjacency matrix previosly saved.

    Args:
        fname (str): _description_

    Returns:
        np.ndarray: _description_
    """

    return np.loadtxt('matrixes/{}'.format(fname))