def longestWordInSen(str):
  str = str.split()
  longestWord = str[0]
  for i in range(len(str)):
    if len(str[i]) > len(longestWord):
      longestWord = str[i]
  return longestWord

print(longestWordInSen("The quick brown fox jumps over the lazy dog"))