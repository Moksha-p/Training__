input = [0, 1, 0, 3, 12]
count = 0
for i in range(len(input)):
    if input[i] != 0:
        input[count] = input[i]
        count += 1
for i in range(count, len(input)):
    input[i] = 0
        
print(input)
