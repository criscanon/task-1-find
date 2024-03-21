"""
Perform linear search to find occurrences of a pattern in a text.

Args:
    text (str): The text to search in.
    pattern (str): The pattern to search for.

Returns:
    int: The number of occurrences of the pattern in the text.
"""
def linear_search(text, pattern):
    occurrences = []                                # O(1)
    for i in range(len(text) - len(pattern) + 1):   # O(n - m + 1) ≈ O(n)
        if text[i:i+len(pattern)] == pattern:       # O(m)
            occurrences.append(i)                   # O(1)
    return len(occurrences)                         # O(1)

# Complexity: O(n - m + 1) * O(m) ≈ O(n) * O(m) ≈ O(n*m)
