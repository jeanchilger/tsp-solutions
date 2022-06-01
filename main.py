import argparse
import statistics

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

    time_history = [h[1] for h in history]
    cost_history = [h[2] for h in history]

    if number_executions > 1:
        print("Execution time: {:0.3f} ({:0.3f}) seconds".format(
                _get_mean(time_history),
                _get_stdev(time_history)))
        print("Cost of the optimal path: {:0.3f} ({:0.3f})".format(
                _get_mean(cost_history),
                _get_stdev(cost_history)))

    else:
        print("Execution time: {:0.3f} seconds".format(time_history[0]))
        print("Cost of the optimal path: {:0.3f}".format(cost_history[0]))


def _run(strategy_name: str, adjacency_mtrx: np.ndarray) -> None:
    strategy = SOLUTIONS_NAME_MAP[args.strategy]()
    path = strategy(adjacency_mtrx)

    return [
        path,
        strategy.exec_time,
        path
        # graph_helper.compute_path_cost(adjacency_mtrx, path)
    ]


def _get_mean(array: np.ndarray) -> float:
    return statistics.mean(array)


def _get_stdev(array: np.ndarray) -> float:
    return statistics.stdev(array)


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