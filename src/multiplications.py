import re


def memory_multiply(memory: str) -> int:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    pairs = re.findall(pattern, memory)
    acc = 0
    pair: tuple[int, int]
    for pair in pairs:
        factor1, factor2 = pair
        acc += int(factor1) * int(factor2)
    return acc
