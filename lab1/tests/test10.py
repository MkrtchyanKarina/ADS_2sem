import unittest
import time
import psutil
from random import randint

from lab1.src.task10 import alice_and_apples


class ApplesTest(unittest.TestCase):
    def test1(self, expected_time=2, expected_memory=256):
        # given
        n = 3
        s = 5
        m = [(2, 3), (10, 5), (5, 10)]
        expected_result = '1 3 2'


        # when
        start = time.perf_counter()
        actual_result = alice_and_apples(n, s, m)
        actual_time = round(time.perf_counter() - start, 2) - start
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_memory, expected_memory)
        self.assertLessEqual(actual_time, expected_time)


    def test2(self, expected_time=2, expected_memory=256):
        # given
        n = 3
        s = 5
        m = [(2, 3), (10, 5), (5, 6)]
        expected_result = -1

        # when
        start = time.perf_counter()
        actual_result = alice_and_apples(n, s, m)
        actual_time = round(time.perf_counter() - start, 2) - start
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(actual_result, expected_result)
        self.assertLessEqual(actual_memory, expected_memory)
        self.assertLessEqual(actual_time, expected_time)


    def test3(self, expected_time=2, expected_memory=256):
        # given
        n = 1000
        s = randint(1, 1000)
        m = [(randint(1, 1000), randint(1, 1000)) for _ in range(n)]

        # when
        start = time.perf_counter()
        actual_result = alice_and_apples(n, s, m)
        actual_time = round(time.perf_counter() - start, 2) - start
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(actual_memory, expected_memory)
        self.assertLessEqual(actual_time, expected_time)


if __name__ == "__main__":
    unittest.main()