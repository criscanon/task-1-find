"""
    Search for all occurrences of a pattern in a text using the Boyer-Moore algorithm.

    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.

    Returns:
        int: The number of occurrences of the pattern in the text.
    """
def boyer_moore_search(text, pattern):
    occurrences = []                                      # O(1)
    m = len(pattern)                                      # O(1)
    n = len(text)                                         # O(1)
    last = {c: pattern.rfind(c) for c in set(pattern)}    # O(m^2), but in practice, often close to O(m)
    i = m - 1                                             # O(1)
    while i < n:                                          # O(n)
        j, k = m - 1, i                                   # O(1)
        while j >= 0 and text[k] == pattern[j]:           # O(m)
            j, k = j - 1, k - 1                           # O(1)
        if j == -1:                                       # O(1)
            occurrences.append(k + 1)                     # O(1)
        i += max(1, j - last.get(text[i], -1))            # O(1)
    return len(occurrences)                               # O(1)

# Complexity: O(m*m) + O(n*m) ≈ O(m) + O(n*m) ≈ O(m*n)
# Average Complexity: O(m+n)