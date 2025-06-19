from src.historian_hysteria import distance, similarity


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


if __name__ == '__main__':
    print(f'The result for day 1 is {perform_day_1()}')
