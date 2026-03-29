from itertools import permutations

def possible_permutations(lst):
    yield from (list(p) for p in permutations(lst))