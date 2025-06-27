from unittest import TestCase

from src.guard_gallivant import count_visited_positions, count_potential_loops


class Test(TestCase):
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

    def test_count_of_visited_positions(self):
        result = count_visited_positions(self.map)
        self.assertEqual(41, result, "There should be 41 visited positions in the map")

        # for this test to work, it's necessary that the previous one has been executed
        result = count_potential_loops(self.map)
        self.assertEqual(6, result, "There should be 6 potential loops in the map")
