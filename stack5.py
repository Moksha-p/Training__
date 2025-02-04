def decode_string(s):
    stack, current_str, current_num = [], "", 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    return current_str

print(decode_string("3[a2[c]]"))  # Output: "accaccacc"
