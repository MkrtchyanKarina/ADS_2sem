import unittest
import time
from random import randint

from lab1.src.task2 import refill


class RefillTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.expected_time = 2

    def test1(self):  # емкость бака = 0 -> никуда не можем доехать
        # given
        d = 950
        m = 0
        n = 4
        s = [200, 375, 550, 750]
        expected_result = -1

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)

    def test2(self):  # нет заправок и расстояние слишком большое
        # given
        d = 950
        m = 400
        n = 0
        s = []
        expected_result = -1

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)

    def test3(self):  # нет заправок, но нам хватит одного бака
        # given
        d = 367
        m = 400
        n = 0
        s = []
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = refill(d, m, n, s)
        t_end = round(time.perf_counter() - t_start, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)

    def test4(self):
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
        self.assertLessEqual(t_end, self.expected_time)

    def test5(self):
        # given
        d = 10
        m = 3
        n = 4
        s = [1, 2, 5, 9]
        expected_result = -1

        # when
        start = time.perf_counter()
        actual_result = refill(d, m, n, s)
        actual_time = round(time.perf_counter() - start, 2)

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_time, self.expected_time)

    def test6(self):
        # given
        d = 200
        m = 250
        n = 2
        s = [100, 150]
        expected_result = 0

        # when
        start = time.perf_counter()
        actual_result = refill(d, m, n, s)
        actual_time = round(time.perf_counter() - start, 2)

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_time, self.expected_time)


    def test7(self):
        # given
        d = 10**5
        m = 400
        n = 300
        s = [i for i in set(randint(1, d) for _ in range(d))]

        # when
        start = time.perf_counter()
        refill(d, m, n, s)
        actual_time = round(time.perf_counter() - start, 2)

        # then
        self.assertLessEqual(actual_time, self.expected_time)


if __name__ == "__main__":
    unittest.main()