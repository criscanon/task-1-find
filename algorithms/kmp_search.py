

def kmp_search(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k-1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    occurrences = []
    m = len(pattern)
    n = len(text)
    pi = compute_prefix_function(pattern + '#' + text)

    for i in range(m+1, m+n+1):
        if pi[i] == m:
            occurrences.append(i - 2*m)
    return occurrences
