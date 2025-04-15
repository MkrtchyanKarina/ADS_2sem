import time
import unittest
from random import randint
import psutil
from lab4.src.task5 import build_prefix
import unittest


class TestBuildPrefix(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(build_prefix(""), [])

    def test_single_character(self):
        self.assertEqual(build_prefix("a"), [0])

    def test_no_repeating_characters(self):
        self.assertEqual(build_prefix("abcde"), [0, 0, 0, 0, 0])

    def test_repeating_characters(self):
        self.assertEqual(build_prefix("aaaa"), [0, 1, 2, 3])

    def test_mixed_characters(self):
        self.assertEqual(build_prefix("ababc"), [0, 0, 1, 2, 0])

    def test_longer_string_with_repeats(self):
        self.assertEqual(build_prefix("abababca"), [0, 0, 1, 2, 3, 4, 0, 1])

    def test_time_memory(self, expected_time=2, expected_memory=256):
        t_start = time.perf_counter()
        result = build_prefix("".join(chr(randint(97, 122)) for _ in range(10**6)))
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(actual_memory, expected_memory)


if __name__ == '__main__':
    unittest.main()




