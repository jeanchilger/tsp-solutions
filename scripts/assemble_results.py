"""
Unites the files from results/ into a single csv file.
"""

import argparse
import csv
from pathlib import Path
import statistics


def main(args: argparse.Namespace) -> None:
    result_dir = Path('results/')

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
                        '{:0.3f}'.format(statistics.mean(cost_history)),
                        '{:0.3f}'.format(statistics.stdev(cost_history)),
                        '{:0.3f}'.format(statistics.mean(time_history)),
                    ])
                    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()


    args, _ = parser.parse_known_args()

    main(args)
