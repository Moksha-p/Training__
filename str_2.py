def remo_dup(Input):
    wo = ""
    for word in Input:
        if word not in wo:
            wo += word
    return wo

Input = "Programming"
print(remo_dup(Input))
