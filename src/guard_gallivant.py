from enum import Enum, auto


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
    initial_position: tuple[int, int]
    current_position: tuple[int, int]
    next_pos: tuple[int, int]
    steps: dict[tuple[int, int], set[Direction]]

    def __init__(self, layout):
        self.lab_map: list[str] = layout.copy()
        self.size = (len(self.lab_map[0]), len(self.lab_map))
        self.direction = Direction.UP
        self.steps = {}

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
        if self.current_position not in self.steps.keys():
            self.steps[self.current_position] = set()
        self.steps[self.current_position].add(self.direction)

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
        if (self.next_pos in self.steps and
                self.direction in self.steps[self.next_pos]):
            return StepResult.LOOP_DETECTED

        # update the current position and exit
        self.current_position = self.next_pos
        return StepResult.STEP_TAKEN

    def walk(self) -> StepResult:
        self.find_initial_position()
        self.current_position = self.find_initial_position()
        result = self.step()
        while result in [StepResult.STEP_TAKEN, StepResult.BLOCK_ENCOUNTERED]:
            result = self.step()
        return result

    def with_obstacle_at(self, obstacle_location: tuple[int, int]):
        obst_x, obst_y = obstacle_location

        map_with_obstacle: list[str] = self.lab_map.copy()
        map_with_obstacle[obst_y] = self.lab_map[obst_y][:obst_x] + '#' + self.lab_map[obst_y][obst_x + 1:]

        return LabMap(map_with_obstacle)


def count_visited_positions(received_map: list[str]) -> int:
    """
    Given a lab map, calculate in advance the trajectory of a patrol, and count the steps.

    :param received_map: Map of the lab.
    :return: Number of steps that the patrol takes before leaving.
    """
    m = LabMap(received_map)
    m.walk()
    return len(m.steps)


def count_potential_loops(received_map: list[str]) -> int:
    """
    Given a lab map, identify the points at which an obstacle would provoke a loop in the patrol trajectory.

    :param received_map: Map that already contains the original patrol trajectory.
    :return: The number of places at which adding an obstacle a patrol loop occurs.
    """
    m = LabMap(received_map)
    m.walk()

    # count how many of the obstacle placements provoke loops
    loops = 0
    for p in m.steps.keys():
        possibly_looped_map = m.with_obstacle_at(p)
        if possibly_looped_map.walk() == StepResult.LOOP_DETECTED:
            loops += 1
    return loops
