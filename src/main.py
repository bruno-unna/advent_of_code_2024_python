import pprint
from pathlib import Path

from src.ceres_search import ceres_search, ceres_x_search
from src.historian_hysteria import distance, similarity
from src.multiplications import memory_multiply, selective_memory_multiply
from src.print_queue import report_totals, Rule, Update
from src.red_nosed_reports import count_safe_reports


def read_lines_from_file(file_name, f):
    """
    Reads lines from a given file, and applies the given transformation for each of them.
    """
    # 1. Get the absolute path of the current file (src/main.py)
    current_file_path = Path(__file__).resolve()

    # 2. Navigate up to the project root.
    # From src/main.py, one .parent goes to src/, another to project_root/
    project_root = current_file_path.parent.parent

    # 3. Construct the path to the resource file
    resource_file_path = project_root / "tests" / "resources" / file_name

    rs = []
    try:
        with open(resource_file_path, 'r') as file:
            for line in file:
                try:
                    rs.append(f(line))
                except ValueError:
                    print(f"Warning: Skipping unparseable line: '{line.strip()}' in {resource_file_path}")
    except FileNotFoundError:
        print(f"Error: The file '{resource_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return rs


def read_block_from_file(file_name) -> str:
    """
    Reads a binary block from a given file, as a string.
    """
    # 1. Get the absolute path of the current file (src/main.py)
    current_file_path = Path(__file__).resolve()

    # 2. Navigate up to the project root.
    # From src/main.py, one .parent goes to src/, another to project_root/
    project_root = current_file_path.parent.parent

    # 3. Construct the path to the resource file
    resource_file_path = project_root / "tests" / "resources" / file_name

    try:
        with open(resource_file_path, 'r', encoding='utf-8') as file:
            block = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{resource_file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return block


def historian_hysteria_challenge() -> dict[str, int]:
    numbers = read_lines_from_file("day1_lists.txt", lambda line: tuple(map(int, line.strip().split())))
    left_numbers = list(map(lambda n: n[0], numbers))
    right_numbers = list(map(lambda n: n[1], numbers))

    return {"distance": distance(left_numbers, right_numbers), "similarity": similarity(left_numbers, right_numbers)}


def red_nosed_reports_challenge() -> dict[str, int]:
    reports = read_lines_from_file("day2_reports.txt", lambda line: list(map(int, line.strip().split())))
    return count_safe_reports(reports)


def mull_it_over_challenge() -> dict[str, int]:
    memory = read_block_from_file("day3_memory.txt")

    return {"multiplication": memory_multiply(memory), "selective_multiplication": selective_memory_multiply(memory)}


def ceres_search_challenge() -> dict[str, int]:
    field = read_lines_from_file("day4_word_search.txt", lambda line: line.strip())

    return {"XMAS count": ceres_search('XMAS', field), "X-MAS count": ceres_x_search('MAS', field)}


def print_queue_challenge() -> dict[str, int]:
    def transformer(line: str) -> Rule:
        s = line.strip().split('|')
        return Rule(int(s[0]), int(s[1]))

    rules = read_lines_from_file("day5_rules.txt", transformer)

    updates = read_lines_from_file("day5_updates.txt", lambda line: Update(list(map(int, line.strip().split(',')))))

    sum_of_middles, sum_of_middles_after_fix = report_totals(rules, updates)

    return {"sum of middle pages": sum_of_middles, "sum of middle pages (fixed updates)": sum_of_middles_after_fix}


if __name__ == '__main__':
    challenges = [
        ("Day 1: Historian Hysteria", historian_hysteria_challenge()),
        ("Day 2: Red-Nosed Reports", red_nosed_reports_challenge()),
        ("Day 3: Mull It Over", mull_it_over_challenge()),
        ("Day 4: Ceres Search", ceres_search_challenge()),
        ("Day 5: Print Queue", print_queue_challenge()),
    ]
    for challenge in challenges:
        print(f'{challenge[0]}: {pprint.pformat(challenge[1])}')
