from src.ceres_search import ceres_search, ceres_x_search
from src.historian_hysteria import distance, similarity
from src.multiplications import memory_multiply, selective_memory_multiply
from src.print_queue import report_totals, Rule, Update
from src.red_nosed_reports import count_safe_reports


def perform_day_1() -> dict[str, int]:
    def read_ints_from_file(file_name) -> list[int]:
        """
        Reads integers from a given file, one per line.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        numbers = []
        try:
            with open(resource_file_path, 'r') as file:
                for line in file:
                    try:
                        number = int(line.strip())
                        numbers.append(number)
                    except ValueError:
                        print(f"Warning: Skipping non-integer line: '{line.strip()}' in {resource_file_path}")
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return numbers

    left_numbers = read_ints_from_file("day1_left.txt")
    right_numbers = read_ints_from_file("day1_right.txt")

    return {"distance": distance(left_numbers, right_numbers), "similarity": similarity(left_numbers, right_numbers)}


def perform_day_2() -> dict[str, int]:
    def read_reports_from_file(file_name) -> list[list[int]]:
        """
        Reads reports (lists of ints) from a given file, one per line.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        reports = []
        try:
            with open(resource_file_path, 'r') as file:
                for line in file:
                    try:
                        reports.append(list(map(int, line.strip().split())))
                    except ValueError:
                        print(f"Warning: Skipping unparseable line: '{line.strip()}' in {resource_file_path}")
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return reports

    return count_safe_reports(read_reports_from_file("day2_reports.txt"))


def perform_day_3() -> dict[str, int]:
    def read_memory_from_file(file_name) -> str:
        """
        Reads a dump of memory from a given file, as a string.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        try:
            with open(resource_file_path, 'r', encoding='utf-8') as file:
                memory = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return memory

    memory = read_memory_from_file("day3_memory.txt")

    return {"multiplication": memory_multiply(memory), "selective_multiplication": selective_memory_multiply(memory)}


def perform_day_4() -> dict[str, int]:
    def read_strs_from_file(file_name) -> list[str]:
        """
        Reads strings from a given file, one per line.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        strs = []
        try:
            with open(resource_file_path, 'r') as file:
                for line in file:
                    s = line.strip()
                    if len(s) > 0:
                        strs.append(s)
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return strs

    field = read_strs_from_file("day4_word_search.txt")

    return {"XMAS count": ceres_search('XMAS', field), "X-MAS count": ceres_x_search('MAS', field)}


def perform_day_5() -> dict[str, int]:
    def read_rules_from_file(file_name) -> list[Rule]:
        """
        Reads rules from a given file, one per line, separated by |.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        rules = []
        try:
            with open(resource_file_path, 'r') as file:
                for line in file:
                    s = line.strip().split('|')
                    rules.append(Rule(int(s[0]), int(s[1])))
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return rules

    def read_updates_from_file(file_name) -> list[Update]:
        """
        Reads updates (lists of ints) from a given file, one per line.
        """
        # 1. Get the absolute path of the current file (src/main.py)
        from pathlib import Path
        current_file_path = Path(__file__).resolve()

        # 2. Navigate up to the project root.
        # From src/main.py, one .parent goes to src/, another to project_root/
        project_root = current_file_path.parent.parent

        # 3. Construct the path to the resource file
        resource_file_path = project_root / "tests" / "resources" / file_name

        updates: list[Update] = []
        try:
            with open(resource_file_path, 'r') as file:
                for line in file:
                    try:
                        updates.append(Update(list(map(int, line.strip().split(',')))))
                    except ValueError:
                        print(f"Warning: Skipping unparseable line: '{line.strip()}' in {resource_file_path}")
        except FileNotFoundError:
            print(f"Error: The file '{resource_file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return updates

    rules = read_rules_from_file("day5_rules.txt")
    updates = read_updates_from_file("day5_updates.txt")

    sum_of_middles, sum_of_middles_after_fix = report_totals(rules, updates)

    return {"sum of middle pages": sum_of_middles, "sum of middle pages (fixed updates)": sum_of_middles_after_fix}


if __name__ == '__main__':
    print(f'The result for day 1 is {perform_day_1()}')
    print(f'The result for day 2 is {perform_day_2()}')
    print(f'The result for day 3 is {perform_day_3()}')
    print(f'The result for day 4 is {perform_day_4()}')
    print(f'The result for day 5 is {perform_day_5()}')
