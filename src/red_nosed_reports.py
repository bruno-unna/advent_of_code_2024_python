from itertools import pairwise


def count_safe_reports(reports: list[list[int]]) -> dict[str, int]:
    def is_safe(report: list[int]) -> bool:
        diffs = [b - a for a, b in pairwise(report)]
        result = True
        if any(x == 0 or x < -3 or x > 3 for x in diffs):
            result = False
        if any(x < 0 for x in diffs) and any(x > 0 for x in diffs):
            result = False
        return result

    def is_safe_dampened(report: list[int]) -> bool:
        if is_safe(report):
            return True
        fixable = False
        for index in range(0, len(report)):
            reduced_report = report[:index] + report[index + 1:]
            if is_safe(reduced_report):
                fixable = True
                break
        return fixable

    return {"undampened": sum(1 for report in reports if is_safe(report)),
            "dampened": sum(1 for report in reports if is_safe_dampened(report))}
