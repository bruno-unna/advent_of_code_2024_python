from unittest import TestCase

from src.red_nosed_reports import count_safe_reports


class Test(TestCase):
    def test_count_safe_reports(self):
        reports = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]
        ]
        safe_count = count_safe_reports(reports)
        self.assertEqual(safe_count["undampened"], 2, "There should be exactly 2 safe reports")
        self.assertEqual(safe_count["dampened"], 4, "There should be exactly 4 dampened safe reports")
