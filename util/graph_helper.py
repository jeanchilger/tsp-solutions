import tsplib95
import numpy as np

def make_adjacency_matrix(problem: tsplib95.models.StandardProblem) -> np.ndarray:
    coords = problem.node_coords

    mtrx = np.zeros(len(coords), len(coords))

    for edge_src in coords.keys():
        for edge_dst in coords.keys():
