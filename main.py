import argparse

import numpy as np
from util import data_helper, graph_helper
from solutions import SOLUTIONS_NAME_MAP

from pprint import pprint


def main(args: argparse.Namespace) -> None:
    """

    Args:
        args (argparse.Namespace): _description_
    """

    number_executions = args.number_executions
    instance_name = args.instance_name
    strategy_name = args.strategy

    problem = data_helper.load_problems(instance_name)
    adjacency_mtrx = graph_helper.make_adjacency_matrix(problem)

    history = []
    for _ in range(number_executions):
        history.append(_run(strategy_name=strategy_name, adjacency_mtrx=adjacency_mtrx))

    pprint(history)


def _run(strategy_name: str, adjacency_mtrx: np.ndarray) -> None:
    strategy = SOLUTIONS_NAME_MAP[args.strategy]()
    path = strategy(adjacency_mtrx)

    return [
        path,
        strategy.exec_time,
        graph_helper.compute_path_cost(adjacency_mtrx, path)
    ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "-i", "--instance-name",
            help="Name of the file instance from National TSP",
            default="wi29", dest="instance_name")

    parser.add_argument(
            "-n", "--number-executions",
            help="Number of times to repeat experiments",
            type=int, default=1, dest="number_executions")

    parser.add_argument(
            "-s", "--strategy",
            help="Solving algorithm to use",
            required=True, dest="strategy")

    args, _ = parser.parse_known_args()

    main(args)