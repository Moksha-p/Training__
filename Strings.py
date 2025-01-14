# Write a Python function to find the longest word in a given sentence.

def longest_word(sentence):
    words = sentence.split()  
    longest = max(words, key=len)  
    return longest

# Example Test Case
sentence = "The quick brown fox jumps over the lazy dog"
print(longest_word(sentence))  

# Write a Python function to check if two given strings are anagrams of each other.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example Test Case
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  
