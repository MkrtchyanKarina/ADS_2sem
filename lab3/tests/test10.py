import time
import unittest
from random import randint

import psutil

from lab3.src.task10 import bellman_ford


class TestBellmanFord(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls. expected_time = 10
        cls.expected_memory = 512

    def test0(self):
        graph = []
        result = bellman_ford(2, 0, graph, 1)
        self.assertEqual(result, ['0', '*'])

    def test1(self):
        graph = [(1, 2, 5)]
        result = bellman_ford(2, 1, graph, 1)
        self.assertEqual(result, ['0', '5'])

    def test2(self):
        graph = [(1, 2, -5)]
        result = bellman_ford(2, 1, graph, 1)
        self.assertEqual(result, ['0', '-5'])


    def test3(self):
        graph = [
            (1, 2, 1),
            (1, 3, 4),
            (2, 3, 2),
            (3, 4, 1)
        ]
        result = bellman_ford(4, 4, graph, 1)
        self.assertEqual(result, ['0', '1', '3', '4'])


    def test4(self):
        graph = [
            (1, 2, 1),
            (3, 4, 1)
        ]
        result = bellman_ford(4, 2, graph, 1)
        self.assertEqual(result, ['0', '1', '*', '*'])


    def test5(self):
        n = 10**3
        m = 10**4
        graph = []

        for i in range(1, m + 1):
            u = (i % n) + 1
            v = ((i + 1) % n) + 1
            weight = randint(-10**9, 10**9)
            graph.append((u, v, weight))

        t_start = time.perf_counter()
        result = bellman_ford(n, m, graph, randint(1, n))
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, self.expected_time)
        self.assertLessEqual(actual_memory, self.expected_memory)



if __name__ == '__main__':
    unittest.main()