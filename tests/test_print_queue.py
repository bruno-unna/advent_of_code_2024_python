from unittest import TestCase

from src.print_queue import sum_middle_pages, Rule, Update


class Test(TestCase):
    def test_print_queue(self):
        rules: list[Rule] = [
            Rule(47, 53),
            Rule(97, 13),
            Rule(97, 61),
            Rule(97, 47),
            Rule(75, 29),
            Rule(61, 13),
            Rule(75, 53),
            Rule(29, 13),
            Rule(97, 29),
            Rule(53, 29),
            Rule(61, 53),
            Rule(97, 53),
            Rule(61, 29),
            Rule(47, 13),
            Rule(75, 47),
            Rule(97, 75),
            Rule(47, 61),
            Rule(75, 61),
            Rule(47, 29),
            Rule(75, 13),
            Rule(53, 13),
        ]
        updates: list[Update] = [
            Update([75, 47, 61, 53, 29]),
            Update([97, 61, 53, 29, 13]),
            Update([75, 29, 13]),
            Update([75, 97, 47, 61, 53]),
            Update([61, 13, 29]),
            Update([97, 13, 75, 29, 47]),
        ]

        good, fixed = sum_middle_pages(rules, updates)
        self.assertEqual(143, good, "The sum of middle pages (valid updates only) should be 143")
        self.assertEqual(123, fixed, "The sum of middle pages (fixed updates only) should be 123")
