from itertools import pairwise


def count_safe_reports(reports: list[list[int]]) -> dict[str, int]:
    def is_safe(record: list[int]) -> bool:
        diffs = [b - a for a, b in pairwise(record)]
        result = True
        if any(x == 0 or x < -3 or x > 3 for x in diffs):
            result = False
        if any(x < 0 for x in diffs) and any(x > 0 for x in diffs):
            result = False
        return result

    def is_safe_dampened(record: list[int]) -> bool:
        return True

    return {"undampened": sum(1 for record in reports if is_safe(record)),
            "dampened": sum(1 for record in reports if is_safe_dampened(record))}
