s = "racecar"
stack = []
n = len(s)
for i in range(n):
    ch = s[i]
    stack.append(ch)
emty = ""
while stack:
    ch = stack[-1]
    emty += ch
    stack.pop()

print(emty)

