class Map:
    """
    Represents the area that the guard will patrol.
    """

    map: list[str]
    size: tuple[int, int]
    direction: str
    position: tuple[int, int]
    next_pos: tuple[int, int]

    def __init__(self, layout):
        self.map: list[str] = layout
        self.size = (len(self.map[0]), len(self.map))
        self.direction = '^'
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.map[j][i] == '^':
                    self.position = (i, j)
                    break

    def step(self) -> bool:

        # mark the current position as visited
        i, j = self.position
        row = self.map[j]
        new_row = row[:i] + 'X' + row[i + 1:]
        self.map[j] = new_row

        # calculate what the next position would be
        match self.direction:
            case '^':
                self.next_pos = (self.position[0], self.position[1] - 1)
            case 'v':
                self.next_pos = (self.position[0], self.position[1] + 1)
            case '<':
                self.next_pos = (self.position[0] - 1, self.position[1])
            case '>':
                self.next_pos = (self.position[0] + 1, self.position[1])

        # if we've reached a boundary, stop
        if self.next_pos[0] < 0 or self.next_pos[0] >= self.size[0] \
                or self.next_pos[1] < 0 or self.next_pos[1] >= self.size[1]:
            return False

        # if we've reached a block, turn right
        ni, nj = self.next_pos
        blocked = self.map[nj][ni] == '#'
        if blocked:
            match self.direction:
                case '^':
                    self.direction = '>'
                case '>':
                    self.direction = 'v'
                case 'v':
                    self.direction = '<'
                case '<':
                    self.direction = '^'
            return True

        # update the current position and exit
        self.position = self.next_pos
        return True

    def how_many_x(self) -> int:
        counter = 0
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.map[j][i] == 'X':
                    counter += 1
        return counter


def count_visited_positions(received_map: list[str]) -> int:
    m = Map(received_map)
    steps = 0
    while m.step():
        steps += 1
    c = m.how_many_x()
    return c
