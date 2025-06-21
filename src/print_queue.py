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


def extract_valid_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> list[list[int]]:
    return list(filter(lambda update: is_valid(update, rules), updates))


def sum_middle_pages(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    valid_updates = extract_valid_updates(rules, updates)
    acc = 0
    for update in valid_updates:
        acc += update[len(update) >> 1]
    return acc
