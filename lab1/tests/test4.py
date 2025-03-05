import unittest
import time
from random import randint

from lab1.src.task4 import intersection_of_segments


class IntersectionTest(unittest.TestCase):
    def test1(self, expected_time=2):
        # given
        n = 3
        s = [(1, 3), (2, 5), (3, 6)]
        expected_result = (1, [3])

        # when
        start = time.perf_counter()
        actual_result = intersection_of_segments(n, s)
        actual_time = round(time.perf_counter() - start, 2) - start

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_time, expected_time)

    def test2(self, expected_time=2):
        # given
        n = 4
        s = [(4, 7), (1, 3), (2, 5), (5, 6)]
        expected_result = (2, [3, 6])

        # when
        start = time.perf_counter()
        actual_result = intersection_of_segments(n, s)
        actual_time = round(time.perf_counter() - start, 2) - start

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_time, expected_time)

    def test3(self, expected_time=2):
        # given
        n = 100
        s = [tuple(sorted([randint(0, 10**9), randint(0, 10**9)])) for _ in range(n)]

        # when
        start = time.perf_counter()
        actual_result = intersection_of_segments(n, s)
        actual_time = round(time.perf_counter() - start, 2) - start

        # then
        self.assertLessEqual(actual_time, expected_time)

    def test4(self, expected_time=2):  # Пример для отрицательных координат
        # given
        n = 100
        s = [tuple(sorted([randint(-10**9, 10**9), randint(-10**9, 10**9)])) for _ in range(n)]

        # when
        start = time.perf_counter()
        actual_result = intersection_of_segments(n, s)
        actual_time = round(time.perf_counter() - start, 2) - start

        # then
        self.assertLessEqual(actual_time, expected_time)



if __name__ == "__main__":
    unittest.main()