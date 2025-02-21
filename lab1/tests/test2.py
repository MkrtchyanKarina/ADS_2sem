import unittest
import time
from random import randint

from lab1.src.task2 import refill


class RefillTest(unittest.TestCase):
    def test1(self, expected_time=2):
        # given
        d = 950
        m = 400
        n = 4
        s = [200, 375, 550, 750]
        expected_result = 2

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)

    def test2(self, expected_time=2):
        # given
        d = 10
        m = 3
        n = 4
        s = [1, 2, 5, 9]
        expected_result = -1

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)

    def test3(self, expected_time=2):
        # given
        d = 200
        m = 250
        n = 2
        s = [100, 150]
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, expected_time)

    def test4(self, expected_time=2):
        # given
        d = 10**5
        m = 400
        n = 300
        s = [i for i in set(randint(1, d) for _ in range(d))]

        # when
        t_start = time.perf_counter()
        refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertLessEqual(t_end, expected_time)


if __name__ == "__main__":
    unittest.main()