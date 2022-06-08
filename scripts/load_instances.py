"""
Loads the instances from the TSPLIB format to adjacency
matrixes, then, saves them.
"""

import argparse
from pathlib import Path

import numpy as np

from util import data_helper, graph_helper


def main(args: argparse.Namespace) -> None:
    data_dir = Path('data/')
    matrixes_dir = Path('matrixes/')

    matrixes_dir.mkdir()

    for instance_path in data_dir.iterdir():

        print(instance_path.stem)

        problem = data_helper.load_problem(instance_path.stem)
        adjacency_mtrx = graph_helper.make_adjacency_matrix(problem)

        np.savetxt(matrixes_dir / instance_path.stem, adjacency_mtrx)

        matrixes_dir
                    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    args, _ = parser.parse_known_args()

    main(args)
