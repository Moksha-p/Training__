from itertools import combinations
input_tuple = (2, 3, 5, 7)
target = 10
result = []
for i in range(len(input_tuple) + 1):
    for j in combinations(input_tuple , i):
        if sum(j) == target:
            result.append(j)
print(result)
        
