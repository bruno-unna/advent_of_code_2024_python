from unittest import TestCase

from src.ceres_search import ceres_search, ceres_x_search


class Test(TestCase):
    def test_ceres_search(self):
        field = [
            'MMMSXXMASM',
            'MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS',
            'SAXAMASAAA',
            'MAMMMXMMMM',
            'MXMXAXMASX'
        ]

        result = ceres_search("XMAS", field)
        self.assertEqual(18, result, "There should be 18 instances of XMAS in the field")

        result = ceres_x_search("MAS", field)
        self.assertEqual(9, result, "There should be 9 instances of MAS in X configuration")
