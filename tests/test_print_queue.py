from unittest import TestCase

from src.print_queue import sum_middle_pages


class Test(TestCase):
    def test_print_queue(self):
        rules: list[tuple[int, int]] = [
            (47, 53),
            (97, 13),
            (97, 61),
            (97, 47),
            (75, 29),
            (61, 13),
            (75, 53),
            (29, 13),
            (97, 29),
            (53, 29),
            (61, 53),
            (97, 53),
            (61, 29),
            (47, 13),
            (75, 47),
            (97, 75),
            (47, 61),
            (75, 61),
            (47, 29),
            (75, 13),
            (53, 13),
        ]
        updates: list[list[int]] = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]

        good, fixed = sum_middle_pages(rules, updates)
        self.assertEqual(143, good, "The sum of middle pages (valid updates only) should be 143")
        self.assertEqual(123, fixed, "The sum of middle pages (fixed updates only) should be 123")
