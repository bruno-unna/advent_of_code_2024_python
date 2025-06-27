from enum import Enum, auto

initial_position: tuple[int, int]


class Direction(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'

    def turn_right(self):
        match self:
            case self.UP:
                return self.RIGHT
            case self.RIGHT:
                return self.DOWN
            case self.DOWN:
                return self.LEFT
            case self.LEFT:
                return self.UP
        return self


class StepResult(Enum):
    STEP_TAKEN = auto()
    LAB_ABANDONED = auto()
    LOOP_DETECTED = auto()
    BLOCK_ENCOUNTERED = auto()


class LabMap:
    """
    Represents the area that the guard will patrol.
    """

    lab_map: list[str]
    size: tuple[int, int]
    direction: Direction
    current_position: tuple[int, int]
    next_pos: tuple[int, int]

    def __init__(self, layout):
        self.lab_map: list[str] = layout.copy()
        self.size = (len(self.lab_map[0]), len(self.lab_map))
        self.direction = Direction.UP

    def find_initial_position(self):
        ini_pos = (0, 0)
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.lab_map[j][i] == Direction.UP.value:
                    ini_pos = (i, j)
                    break
        return ini_pos

    def step(self) -> StepResult:

        # mark the current position as visited
        i, j = self.current_position
        row = self.lab_map[j]
        new_row = row[:i] + self.direction.value + row[i + 1:]
        self.lab_map[j] = new_row

        # calculate what the next position would be
        match self.direction:
            case Direction.UP:
                self.next_pos = (self.current_position[0], self.current_position[1] - 1)
            case Direction.DOWN:
                self.next_pos = (self.current_position[0], self.current_position[1] + 1)
            case Direction.LEFT:
                self.next_pos = (self.current_position[0] - 1, self.current_position[1])
            case Direction.RIGHT:
                self.next_pos = (self.current_position[0] + 1, self.current_position[1])

        # if we've reached a boundary, stop
        if self.next_pos[0] < 0 or self.next_pos[0] >= self.size[0] \
                or self.next_pos[1] < 0 or self.next_pos[1] >= self.size[1]:
            return StepResult.LAB_ABANDONED

        # if we've reached a block, turn right
        ni, nj = self.next_pos
        blocked = self.lab_map[nj][ni] == '#'
        if blocked:
            self.direction = self.direction.turn_right()
            return StepResult.BLOCK_ENCOUNTERED

        # if we've been here before, in the same situation, it's a loop
        ni, nj = self.next_pos
        if self.lab_map[nj][ni] == self.direction.value:
            return StepResult.LOOP_DETECTED

        # update the current position and exit
        self.current_position = self.next_pos
        return StepResult.STEP_TAKEN

    def walk(self) -> StepResult:
        self.current_position = initial_position
        result = self.step()
        while result in [StepResult.STEP_TAKEN, StepResult.BLOCK_ENCOUNTERED]:
            result = self.step()
        return result

    def how_many_x(self) -> int:
        counter = 0
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if self.lab_map[j][i] in [dir.value for dir in Direction]:
                    counter += 1
        return counter

    def with_obstacle_at(self, obstacle_location: tuple[int, int]):
        obst_x, obst_y = obstacle_location

        map_with_obstacle: list[str] = self.lab_map.copy()
        map_with_obstacle[obst_y] = self.lab_map[obst_y][:obst_x] + '#' + self.lab_map[obst_y][obst_x + 1:]

        return LabMap(map_with_obstacle)


def count_visited_positions(received_map: list[str]) -> int:
    m = LabMap(received_map)
    global initial_position
    initial_position = m.find_initial_position()
    m.walk()
    return m.how_many_x()


def count_potential_loops(received_map: list[str]) -> int:
    """
    Given a lab map, identify the points at which an obstacle would provoke a loop in the patrol trajectory.

    :param received_map: Map that already contains the original patrol trajectory.
    :return: The number of places at which adding an obstacle a patrol loop occurs.
    """
    m = LabMap(received_map)
    global initial_position
    initial_position = m.find_initial_position()
    m.walk()

    # find potential obstacle placements
    points: list[tuple[int, int]] = []
    for i in range(0, m.size[0]):
        for j in range(0, m.size[1]):
            if m.lab_map[j][i] in [d.value for d in Direction]:
                p = (i, j)
                points.append(p)

    m = LabMap(received_map)

    # count how many of the obstacle placements provoke loops
    loops = 0
    for p in points:
        possibly_looped_map = m.with_obstacle_at(p)
        r = possibly_looped_map.walk()
        if r == StepResult.LOOP_DETECTED:
            loops += 1
    return loops
