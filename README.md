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
                    Number of times to repeat experiments
-s STRATEGY, --strategy STRATEGY
                    Solving algorithm to use
```

You can type `python main.py --help` to get more information on the command line options.

## Available Solving Algorithms

* **`random`:**
