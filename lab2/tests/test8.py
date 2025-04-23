import unittest
import time
from random import randint
import psutil

from lab2.src.task8 import calculate_height


class TestHeightBFS(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.expected_time = 2
        cls.expected_memory = 256

    def test0(self):
        # given
        count = 0
        nodes = []
        expected_result = 0

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)

    def test1(self):
        # given
        count = 1
        nodes = [(1, 0, 0)]
        expected_result = 1

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)

    def test2(self):
        # given
        nodes = [
            (1, 2, 3),  # Узел 1 с левым 2 и правым 3
            (2, 4, 5),  # Узел 2 с левым 4 и правым 5
            (3, 0, 0),  # Узел 3 без детей
            (4, 0, 0),  # Узел 4 без детей
            (5, 0, 0)  # Узел 5 без детей
        ]
        count = 5
        expected_result = 3

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)

    def test3(self):
        # given
        nodes = [
            (1, 2, 3),  # Узел 1 с левым 2 и правым 3
            (1, 0, 4),  # Узел 2 (дубликат) с правым ребенком 4
            (3, 0, 0),  # Узел 3 без детей
            (2, 0, 0)  # Узел 4 без детей
        ]
        count = 4
        expected_result = 3

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)

    def test4(self):
        # given
        count = 3
        nodes = [
            (1, 2, 0),  # Узел 1 с левым 2 и без правого ребенка
            (2, 3, 0),  # Узел 2 с левым 3 и без правого ребенка
            (3, 0, 0)  # Узел 3 без детей
        ]
        expected_result = 3

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)



    def test5(self):
        # given
        count = 2*10**5
        nodes = []
        for i in range(1, count + 1):
            left = 2*i if 2*i < count else 0
            right = 2*i + 1 if 2*i + 1 < count else 0
            key = randint(-10**9, 10**9)
            nodes += [(key, left, right)]
        expected_result = 18

        # when
        t_start = time.perf_counter()
        result = calculate_height(count, nodes)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)




if __name__ == "__main__":
    unittest.main()