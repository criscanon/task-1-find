
def boyer_moore_search(text, pattern):
    occurrences = []
    m = len(pattern)
    n = len(text)
    last = {c: pattern.rfind(c) for c in set(pattern)}
    i = m - 1
    while i < n:
        j, k = m - 1, i
        while j >= 0 and text[k] == pattern[j]:
            j, k = j - 1, k - 1
        if j == -1:
            occurrences.append(k + 1)
        i += max(1, j - last.get(text[i], -1))
    return occurrences
