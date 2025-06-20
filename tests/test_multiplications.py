from unittest import TestCase

from src.multiplications import memory_multiply


class Test(TestCase):
    def test_multiplications(self):
        memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        result = memory_multiply(memory)
        self.assertEqual(161, result, "The memory should multiply to 161")
