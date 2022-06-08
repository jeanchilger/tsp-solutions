import tsplib95


def load_problem(fname: str) -> tsplib95.models.StandardProblem:
    """
    Loads the problems from file, and returns
    a list with them.

    Args:
        fname (str): _description_

    Returns:
        tsplib95.models.StandardProblem: _description_
    """

    return tsplib95.load("data/{}.tsp".format(fname))