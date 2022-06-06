import argparse
import csv
from pathlib import Path
import statistics

import numpy as np
from util import data_helper, graph_helper
from solutions import SOLUTIONS_NAME_MAP

from pprint import pp, pprint


def main(args: argparse.Namespace) -> None:
    number_executions = args.number_executions
    instance_name = args.instance_name
    strategy_name = args.strategy
    output_dir = args.output_dir

    problem = data_helper.load_problems(instance_name)
    adjacency_mtrx = graph_helper.make_adjacency_matrix(problem)

    timelimit = (
        args.timelimit
        if args.timelimit > 0
        else 0.06 * problem.dimension
    )

    strategy_kwargs = {
        'timelimit': timelimit,
    }

    history = []
    for _ in range(number_executions):
        hist_entry = _run(strategy_name, adjacency_mtrx, strategy_kwargs)
        history.append(hist_entry)

    write_report(history, output_dir, strategy_name, instance_name)


def _run(
        strategy_name: str, adjacency_mtrx: np.ndarray,
        strategy_kwargs: dict) -> None:
    strategy = SOLUTIONS_NAME_MAP[strategy_name]()
    path = strategy(adjacency_mtrx, **strategy_kwargs)

    return [
        path,
        strategy.evaluate(adjacency_mtrx, path),
        strategy.exec_time,
    ]


def write_report(
        history: list, output_dir: Path,
        strategy_name: str, instance_name: str) -> None:
    cost_history = [h[1] for h in history]
    time_history = [h[2] for h in history]

    if len(history) > 1:
        report_dir = output_dir / instance_name / strategy_name
        report_dir.mkdir(parents=True, exist_ok=True)

        with open(report_dir / 'output.csv', 'w') as report_file:
            csv_writer = csv.writer(report_file)

            csv_writer.writerow([
                'instance',
                'algorithm',
                'cost',
                'exec_time',
            ])

            for h in history:
                csv_writer.writerow([
                    instance_name,
                    strategy_name,
                    h[1],
                    '{:0.4f}'.format(h[2]),
                ])

            print('Execution time: {:0.3f} ({:0.3f}) seconds'.format(
                    _get_mean(time_history),
                    _get_stdev(time_history)))
            print('Cost of the optimal path: {:0.3f} ({:0.3f})'.format(
                    _get_mean(cost_history),
                    _get_stdev(cost_history)))

    else:
        print('Execution time: {:0.3f} seconds'.format(time_history[0]))
        print('Cost of the optimal path: {:0.3f}'.format(cost_history[0]))


def _get_mean(array: np.ndarray) -> float:
    return statistics.mean(array)


def _get_stdev(array: np.ndarray) -> float:
    return statistics.stdev(array)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
            '-i', '--instance-name',
            help='Name of the file instance from National TSP',
            default='wi29', dest='instance_name')

    parser.add_argument(
            '-n', '--number-executions',
            help='Number of times to repeat experiments',
            type=int, default=1, dest='number_executions')

    parser.add_argument(
            '-s', '--strategy',
            help='Solving algorithm to use',
            nargs='?', choices=[*SOLUTIONS_NAME_MAP.keys()],
            required=True, dest='strategy')
    
    parser.add_argument(
            '-t', '--timelimit',
            help='Maximum time to wait for a solution (in seconds). \
                    Set to -1 for adaptive timelimit',
            type=int, default=-1, dest='timelimit')
    
    parser .add_argument(
            '-o', '--output-dir',
            help='Path where to save the output files',
            type=Path, default='results/', dest='output_dir')

    args, _ = parser.parse_known_args()

    main(args)
