def sec_lar(lst):
    new_lst = sorted(lst)
    return new_lst[-2]


lst = [1, 3, 4, 2]
print(sec_lar(lst))