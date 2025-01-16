def is_rotation(str1, str2):
    return len(str1) == len(str2) and str2 in str1 + str1

print(is_rotation("abcde", "cdeab"))