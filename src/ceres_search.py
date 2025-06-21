def ceres_search(needle: str, field: list[str]) -> int:
    directions: list[tuple[int, int]] = [
        (1, 0),  # right
        (-1, 0),  # left
        (0, -1),  # up
        (0, 1),  # down
        (1, -1),  # up-right
        (1, 1),  # down-right
        (-1, -1),  # up-left
        (-1, 1),  # down-left
    ]
    field_size = (len(field[0]), len(field))

    def is_match(part_needle: str, position: tuple[int, int], direction: tuple[int, int]) -> bool:
        if len(part_needle) == 0:
            return True
        lx, ly = position
        dx, dy = direction
        if lx < 0 or lx >= field_size[0] or ly < 0 or ly >= field_size[1]:
            return False
        return part_needle[0] == field[ly][lx] and is_match(part_needle[1:], (lx + dx, ly + dy), direction)

    count = 0
    for x in range(0, field_size[0]):
        for y in range(0, field_size[1]):
            count += sum(1 for direction in directions if is_match(needle, (x, y), direction))

    return count


def ceres_x_search(needle: str, field: list[str]) -> int:
    if len(needle) % 2 != 1:
        return 0  # for this to work we need the word to have a central element
    directions: dict[str, tuple[int, int]] = {
        'up-right': (1, -1),
        'down-right': (1, 1),
        'up-left': (-1, -1),
        'down-left': (-1, 1),
    }
    field_size = (len(field[0]), len(field))
    half_size = len(needle) >> 1
    central_letter = needle[half_size]

    def is_match(part_needle: str, position: tuple[int, int], direction: tuple[int, int]) -> bool:
        if len(part_needle) == 0:
            return True
        lx, ly = position
        dx, dy = direction
        if lx < 0 or lx >= field_size[0] or ly < 0 or ly >= field_size[1]:
            return False
        return part_needle[0] == field[ly][lx] and is_match(part_needle[1:], (lx + dx, ly + dy), direction)

    def examine_cross(needle: str, x: int, y: int, half_size: int) -> bool:
        first_arm = (is_match(needle, (x - half_size, y - half_size), directions['down-right']) or
                     is_match(needle, (x + half_size, y + half_size), directions['up-left']))
        second_arm = (is_match(needle, (x - half_size, y + half_size), directions['up-right']) or
                      is_match(needle, (x + half_size, y - half_size), directions['down-left']))
        return first_arm and second_arm

    count = 0
    for x in range(0, field_size[0]):
        for y in range(0, field_size[1]):
            if field[y][x] == central_letter and examine_cross(needle, x, y, half_size):
                count += 1

    return count
