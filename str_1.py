def frequency(s):
    freq = {}

    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

s = "apple"
print(frequency(s))