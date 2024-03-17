# tests/test_search_algorithms.py

import unittest
from algorithms.linear_search import linear_search
from algorithms.kmp_search import kmp_search
from algorithms.boyer_moore_search import boyer_moore_search
from metrics.metrics import measure_time_in_milliseconds, count_basic_operations, count_function_calls

class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_search(self):
        text = "ababcababcabcabc"
        pattern = "abc"

        result, avg_exec_time = measure_time_in_milliseconds(linear_search, text, pattern, num_runs=10)
        _, basic_ops = count_basic_operations(linear_search, text, pattern)
        _, func_calls = count_function_calls(linear_search, text, pattern)

        self.assertEqual(result, [2, 5, 8, 11, 14])
        self.assertGreaterEqual(avg_exec_time, 0)
        self.assertGreaterEqual(basic_ops, 0)
        self.assertGreaterEqual(func_calls, 0)

    def test_kmp_search(self):
        text = "ababcababcabcabc"
        pattern = "abc"

        result, avg_exec_time = measure_time_in_milliseconds(kmp_search, text, pattern, num_runs=10)
        _, basic_ops = count_basic_operations(kmp_search, text, pattern)
        _, func_calls = count_function_calls(kmp_search, text, pattern)

        self.assertEqual(result, [2, 5, 8, 11, 14])
        self.assertGreaterEqual(avg_exec_time, 0)
        self.assertGreaterEqual(basic_ops, 0)
        self.assertGreaterEqual(func_calls, 0)

    def test_boyer_moore_search(self):
        text = "ababcababcabcabc"
        pattern = "abc"

        result, avg_exec_time = measure_time_in_milliseconds(boyer_moore_search, text, pattern, num_runs=10)
        _, basic_ops = count_basic_operations(boyer_moore_search, text, pattern)
        _, func_calls = count_function_calls(boyer_moore_search, text, pattern)

        self.assertEqual(result, [2, 5, 8, 11, 14])
        self.assertGreaterEqual(avg_exec_time, 0)
        self.assertGreaterEqual(basic_ops, 0)
        self.assertGreaterEqual(func_calls, 0)

if __name__ == '__main__':
    unittest.main()
