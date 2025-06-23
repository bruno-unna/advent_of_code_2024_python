from unittest import TestCase

from src.guard_gallivant import count_visited_positions


class Test(TestCase):
    def test_guard_gallivant(self):
        map = [
            '....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...',
        ]

        result = count_visited_positions(map)
        self.assertEqual(41, result, "There should be 41 visited positions in the map")
