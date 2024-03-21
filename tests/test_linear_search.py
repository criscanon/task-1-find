import unittest
from algorithms.linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_occurrences_large_text(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla euismod dolor id dui ultrices."
        pattern = "dolor"
        expected_occurrences = 2
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_long_pattern(self):
        text = "This is a simple text for testing linear search algorithm."
        pattern = "algorithmlinearsearchtestingsimple"
        expected_occurrences = 0
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_pattern_repetitions(self):
        text = "abcabcabcabcabc"
        pattern = "abc"
        expected_occurrences = 5
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_text(self):
        text = ""
        pattern = "pattern"
        expected_occurrences = 0
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_pattern(self):
        text = "text"
        pattern = ""
        expected_occurrences = 0
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_text_and_pattern_empty(self):
        text = ""
        pattern = ""
        expected_occurrences = 0
        result = linear_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

if __name__ == '__main__':
    unittest.main()
