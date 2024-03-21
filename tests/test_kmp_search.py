import unittest
from algorithms.kmp_search import kmp_search

class TestKmpSearch(unittest.TestCase):
    def test_occurrences_repetitive_structure(self):
        text = "abcabcdabcabcdabcabcd"
        pattern = "abcabcd"
        expected_occurrences = 3
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_many_prefix_suffix_matches(self):
        text = "abacabacabacab"
        pattern = "abacab"
        expected_occurrences = 3
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_random_text(self):
        text = "This is a random text for testing KMP search algorithm."
        pattern = "algorithmKMPsearchtestingrandom"
        expected_occurrences = 1
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_text(self):
        text = ""
        pattern = "pattern"
        expected_occurrences = 0
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_empty_pattern(self):
        text = "text"
        pattern = ""
        expected_occurrences = 0
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

    def test_occurrences_text_and_pattern_empty(self):
        text = ""
        pattern = ""
        expected_occurrences = 0
        result = kmp_search(text, pattern)
        self.assertEqual(result, expected_occurrences)

if __name__ == '__main__':
    unittest.main()
