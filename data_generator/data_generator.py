
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_data(text_length, pattern_length):
    text = ""
    for i in range (text_length // 10):
        text = text + "ABCABCABC"
    pattern = "ABCABCABCD"
    return text, pattern
