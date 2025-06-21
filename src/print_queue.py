from itertools import permutations
from operator import contains


def explode_update(update: list[int]) -> list[tuple[int, int]]:
    tuples: list[tuple[int, int]] = []
    for left in range(0, len(update) - 1):
        for right in range(left + 1, len(update)):
            tuples.append((update[left], update[right]))
    return tuples


def is_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    if len(update) % 2 == 0:  # this doesn't work for updates with even number of elements
        return False
    update_tuples: list[tuple[int, int]] = explode_update(update)
    return all(map(lambda t: contains(rules, t), update_tuples))


def triage_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    valid_updates = []
    invalid_updates = []
    for u in updates:
        if is_valid(u, rules):
            valid_updates.append(u)
        else:
            invalid_updates.append(u)
    return valid_updates, invalid_updates


def fix(rules: list[tuple[int, int]], bad_updates: list[list[int]]) -> list[list[int]]:
    def fix_update(bad_update: list[int]) -> list[int]:
        candidate_rules: list[tuple[int, int]] = list(
            filter(lambda r: r[0] in bad_update and r[1] in bad_update, rules))

        for permutation in permutations(bad_update):
            candidate_update = list(permutation)
            if is_valid(candidate_update, candidate_rules):
                return candidate_update
        return []

    fixed_updates = []
    for bu in bad_updates:
        fixed_updates.append(fix_update(bu))
    return fixed_updates


def sum_middle_pages(rules: list[tuple[int, int]], updates: list[list[int]]) -> tuple[int, int]:
    def accumulate(us: list[list[int]]) -> int:
        acc = 0
        for u in us:
            acc += u[len(u) >> 1]
        return acc

    valid, invalid = triage_updates(rules, updates)
    fixed = fix(rules, invalid)
    n_valid, n_fixed = map(accumulate, (valid, fixed))
    return n_valid, n_fixed
