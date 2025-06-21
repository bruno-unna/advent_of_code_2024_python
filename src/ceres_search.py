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
