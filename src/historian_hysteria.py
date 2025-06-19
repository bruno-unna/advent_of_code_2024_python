def distance(left: list[int], right: list[int]) -> int | None:
    def subtract_tuple_elements(tup) -> int:
        return abs(tup[0] - tup[1])

    if len(left) != len(right):
        return None
    tuples = zip(sorted(left), sorted(right))
    diffs = map(subtract_tuple_elements, tuples)
    return sum(diffs)
