def char_frequency(s):
    return {char: s.count(char) for char in s}

print(char_frequency("apple"))
