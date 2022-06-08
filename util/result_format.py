"""
Utilities to formatting the results according 
to the specified in the task
"""

import argparse
import csv
import shutil
import statistics
from pathlib import Path
from typing import Union


PathOrStr = Union[str, Path]


def assemble_results(results_path: PathOrStr) -> None:
    """
    Assembles the results from `results_path` into a single
    report file.

    Args:
        results_path (str): Path to the results' root folder.
    """

    result_dir = Path(results_path)

    with open(result_dir / 'report.csv', 'w') as report_file:
        report_writer = csv.writer(report_file)

        report_writer.writerow([
            'instancia',
            'autoria',
            'algoritmo',
            'q-medio',
            'q-desvio',
            't-medio',
        ])

        for instance in result_dir.iterdir():
            
            if instance.is_file(): continue
            
            for strategy in instance.iterdir():
    
                if strategy.is_file(): continue

                with open(strategy / 'output.csv', 'r') as output_file:
                    output_reader = csv.reader(output_file)

                    next(output_reader)

                    cost_history = []
                    time_history = []

                    for row in output_reader:
                        instance_name, algorithm, cost, exec_time = row
                        cost_history.append(float(cost))
                        time_history.append(float(exec_time))

                    report_writer.writerow([
                        instance_name,
                        'Jean',
                        algorithm,
                        '{:0d}'.format(round(statistics.mean(cost_history))),
                        '{:0.2f}'.format(statistics.stdev(cost_history)),
                        '{:0d}'.format(round(statistics.mean(time_history))),
                    ])


def copy_file(src_path: PathOrStr, dst_path: PathOrStr) -> None:
    """
    Copies a file from src_path to dst_path.

    Args:
        src_path (PathOrStr): _description_
        dst_path (PathOrStr): _description_
    """

    shutil.copy(src_path, dst_path)
    