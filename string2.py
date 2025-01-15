def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

print(remove_duplicates("programming"))
