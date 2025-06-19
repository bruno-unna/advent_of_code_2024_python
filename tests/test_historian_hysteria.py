from unittest import TestCase

from src.historian_hysteria import distance, similarity


class Test(TestCase):
    def test_distance(self):
        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]
        d = distance(left, right)
        self.assertEqual(d, 11, "The distance between the lists should be 11")

    def test_similarity(self):
        left = [3, 4, 2, 1, 3, 3]
        right = [4, 3, 5, 3, 9, 3]
        s = similarity(left, right)
        self.assertEqual(s, 31, "The similarity score between the lists should be 31")
