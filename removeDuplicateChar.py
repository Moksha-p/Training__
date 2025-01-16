def removeDuplicateChar(s):
 seen = set()
 result = []

 for char in s:
  if char not in seen:
   seen.add(char)
   result.append(char)
 return ''.join(result)

print(removeDuplicateChar("programming"))
