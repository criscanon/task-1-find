def generate_data(text_length):
    text = ""
    for _ in range (text_length // 9):
        text = text + "ABCABCABC"
    return text

#ABCABCABCABCABCABC
#         ABCABCABCD