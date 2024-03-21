import unittest
from algorithms.boyer_moore_search import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):
    def test_occurrences_last_character(self):
        text = "This is a simple text for testing the Boyer-Moore algorithm."
        pattern = "m"
        expected_occurrences = 1
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_many_different_characters(self):
        text = "abcde" * 1000
        pattern = "fgh"
        expected_occurrences = 0
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_long_pattern_few_repeated_characters(self):
        text = "ab" * 1000
        pattern = "abababab"
        expected_occurrences = 996
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_text(self):
        text = ""
        pattern = "pattern"
        expected_occurrences = 0
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_pattern(self):
        text = "text"
        pattern = ""
        expected_occurrences = 0
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_text_and_pattern_empty(self):
        text = ""
        pattern = ""
        expected_occurrences = 0
        result = boyer_moore_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

if __name__ == '__main__':
    unittest.main()
