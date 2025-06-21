def is_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    return False


def extract_valid_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> list[list[int]]:
    return list(filter(lambda update: is_valid(update, rules), updates))


def sum_middle_pages(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    valid_updates = extract_valid_updates(rules, updates)
    acc = 0
    for update in valid_updates:
        acc += update[len(update) >> 1]
    return acc
