import time
import unittest
from random import randint
import psutil
from lab4.src.task1 import naive_string_search


class TestNaiveStringSearch(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(naive_string_search("aba", "abaCaba"), (2, [1, 5]))
        self.assertEqual(naive_string_search("abc", "ababcabc"), (2, [3, 6]))
        self.assertEqual(naive_string_search("xyz", "abcdefg"), (0, []))
        self.assertEqual(naive_string_search("", "abc"), (0, []))
        self.assertEqual(naive_string_search("a", ""), (0, []))
        self.assertEqual(naive_string_search("abcde", "abc"), (0, []))

    def test_time_memory(self, expected_time=2, expected_memory=256):
        long_p = "a" * 5*10**3
        long_t = "a" * 10**4 + "b"


        t_start = time.perf_counter()
        result = naive_string_search(long_p, long_t)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(actual_memory, expected_memory)
        self.assertTrue(result[0], 5 * 10 ** 3)

    def test_time_memory_random(self, expected_time=2, expected_memory=256):
        long_p = "".join(chr(randint(97, 122)) for _ in range(randint(1, 10**4)))
        long_t = "".join(chr(randint(97, 122)) for _ in range(10**4))


        t_start = time.perf_counter()
        result = naive_string_search(long_p, long_t)
        t_end = round(time.perf_counter() - t_start, 2)
        actual_memory = round(psutil.Process().memory_info().rss / 1024 ** 2, 2)

        # then
        self.assertLessEqual(t_end, expected_time)
        self.assertLessEqual(actual_memory, expected_memory)




if __name__ == "__main__":
    unittest.main()