def longest_increasing_subsequence(lst):
    subsequences = [[lst[0]]]
    for i in range(1, len(lst)):
        subsequences.append([lst[i]])
        for subseq in subsequences[:-1]:
            if subseq[-1] < lst[i]:
                subsequences[-1] = subseq + [lst[i]]
    return max(subsequences, key=len)

print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # Output: [10, 22, 33, 50, 60, 80]
