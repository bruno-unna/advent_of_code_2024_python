def is_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    return False


def extract_valid_updates(rules: list[tuple[int, int]], updates: list[list[int]]) -> list[list[int]]:
    return list(filter(lambda update: is_valid(update, rules), updates))


def sum_middle_pages(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    return 0
