import argparse
from util import data_helper, graph_helper

from pprint import pprint


def main(args: argparse.Namespace) -> None:
    """

    Args:
        args (argparse.Namespace): _description_
    """

    number_executions = args.number_executions
    instance_name = args.instance_name

    problem = data_helper.load_problems(instance_name)
    adjacency_mtrx = graph_helper.make_adjacency_matrix(problem)

    pprint(adjacency_mtrx)

    for _ in range(number_executions):
        _run()


def _run() -> None:
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "-i", "--instance-name",
            help="Name of the file instance from National TSP",
            default="wi29", dest="instance_name")

    parser.add_argument(
            "-n", "--number-executions",
            help="Number of times to repeat experiments",
            default=1, dest="number_executions")

    args, _ = parser.parse_known_args()

    main(args)