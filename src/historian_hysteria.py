from collections import Counter


def distance(left: list[int], right: list[int]) -> int | None:
    def subtract_tuple_elements(tup) -> int:
        return abs(tup[0] - tup[1])

    if len(left) != len(right):
        return None
    tuples = zip(sorted(left), sorted(right))
    diffs = map(subtract_tuple_elements, tuples)
    return sum(diffs)


def similarity(left: list[int], right: list[int]) -> int | None:
    left_counter = Counter(left)
    right_counter = Counter(right)
    acc = 0
    for element in left_counter.keys():
        acc += element * left_counter[element] * right_counter[element]
    return acc
