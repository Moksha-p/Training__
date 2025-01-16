def countChar(s):
  count = 1 
  result = []
  n = len(s)
  for i in range(1, n):
    if s[i - 1] == s[i]:
      count += 1
    else :  
        result.append(s[i-1] + str(count))
        count = 1
  result.append(s[-1] + str(count))
  return ''.join(result)

s = "aaabbc"
print(countChar(s))   