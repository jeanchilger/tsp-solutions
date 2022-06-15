from .random import Random1, Random2
from .brute_force import BruteForce
from .local_search import BLPMsh, BLPM2opt


SOLUTIONS_NAME_MAP = {
    "BTA": Random1,
    "random1": Random1,
    "random2": Random2,
    "brute-force": BruteForce,
    "BLPMsh": BLPMsh,
    "BLPM2opt": BLPM2opt,
}
