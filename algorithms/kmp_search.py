"""
Knuth-Morris-Pratt algorithm for string searching.

Args:
    text (str): The text to search in.
    pattern (str): The pattern to search for.

Returns:
    int: The number of occurrences of the pattern in the text.
"""
def kmp_search(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)                                # O(1)
        pi = [0] * m                                    # O(m)
        k = 0                                           # O(1)
        for q in range(1, m):                           # O(m)
            while k > 0 and pattern[k] != pattern[q]:   # O(m)
                k = pi[k-1]                             # O(1)
            if pattern[k] == pattern[q]:                # O(1)
                k += 1                                  # O(1)
            pi[q] = k                                   # O(1)
        return pi                                       # O(1)
                                                        # partial = O(m*m)
    occurrences = []                                    # O(1)
    m = len(pattern)                                    # O(1)
    n = len(text)                                       # O(1)
    pi = compute_prefix_function(pattern)               # O(1)
    q = 0                                               # O(1)

    for i in range(n):                                  # O(n)
        while q > 0 and pattern[q] != text[i]:          # O(n)
            q = pi[q-1]                                 # O(1)
        if pattern[q] == text[i]:                       # O(1)
            q += 1                                      # O(1)
        if q == m:                                      # O(1)
            occurrences.append(i - m + 1)               # O(1)
            q = pi[q-1]                                 # O(1)

    return len(occurrences)                             # O(1)

# Complexity: O(n*n) + O(m*m) ≈ O(n) + O(m) ≈ O(n+m)
# "AAAAAAAAA"
