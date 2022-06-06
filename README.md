# Travelling Salesman Problem Solutions

Experiment using several different solutions to the TSP

## Installation

Download the code and install the python dependencies:

```
pip install -r requirements.txt
```

## Running

The entry point of the program is the `main.py` file. There are a few options available:

```
-h, --help          show this help message and exit
-i INSTANCE_NAME, --instance-name INSTANCE_NAME
                    Name of the file instance from National TSP
-n NUMBER_EXECUTIONS, --number-executions NUMBER_EXECUTIONS
                    Number of times to repeat experiments.
                    Defaults to 1.
-s STRATEGY, --strategy STRATEGY
                    Solving algorithm to use.
-t TIMELIMIT, --timelimit TIMELIMIT
                    Maximum time to wait for a solution (in seconds). Set to -1 for adaptive timelimit.
                    Defaults to -1.
-o OUTPUT_DIR, --output-dir OUTPUT_DIR
                    Path where to save the output files.
                    Defaults to "results/"
```

You can type `python main.py --help` to get more information on the command line options.

## Available Solving Algorithms

In this section the available solving algorithms (aka strategies) are explained.

* **`random1`:** The `random1` strategy simply shuffles the nodes of the graph;
* **`random2`:** The `random2` strategy builds the path by selecting randomically each node at a time;
* **`brute-force`:** The `brute-force` strategy tries to explore all possible solutions and select the best;
