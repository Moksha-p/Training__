# 1. Find the Frequency of Each Character
from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

print(char_frequency("apple"))

# 2. Remove Duplicates from a String
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

print(remove_duplicates("programming"))

# 3. Find the First Non-Repeating Character
def first_non_repeating(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

print(first_non_repeating("swiss"))

# 4. Check if a String is a Rotation of Another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

print(is_rotation("abcde", "cdeab"))

# 5. Compress a String Using the Counts of Repeated Characters
def compress_string(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

print(compress_string("aaabbc"))
