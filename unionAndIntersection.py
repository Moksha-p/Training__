input1 = [1, 2, 3]
input2 = [2, 3, 4]

union = list(set(input1) | set(input2))
intersection = list(set(input1) & set(input2))

print("Union: ",sorted(union))
print("Intersection: ",sorted(intersection))

