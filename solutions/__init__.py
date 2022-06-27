from .random import Random1, Random2
from .brute_force import BruteForce
from .local_search import BLPMsh, BLMMsh, BLPM2opt, BLMM2opt
from .tabu_search import BTsh, BT2opt


SOLUTIONS_NAME_MAP = {
    'BTA': Random1,
    'random1': Random1,
    'random2': Random2,
    'brute-force': BruteForce,
    'BLPMsh': BLPMsh,
    'BLMMsh': BLMMsh,
    'BLPM2opt': BLPM2opt,
    'BLMM2opt': BLMM2opt,
    'BTsh': BTsh,
    'BT2opt': BT2opt,
}
