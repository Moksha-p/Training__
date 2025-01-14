# Find the longest word in a given sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("The quick brown fox jumps over the lazy dog"))
print(longest_word("Brown Horses play in the Park"))  

# Check if two given strings are anagrams of each other
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))