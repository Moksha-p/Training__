def countChar(str):
  dict = {}
  for i in str:
    dict[i] = str.count(i)

  return dict

str = "apple"
print(countChar(str))   