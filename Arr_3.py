def union_intersection(arr1, arr2):
    union = set(arr1)
    union1 = set(arr2)
    union_res = list(union.union(union1))
    inter_res = list(union.intersection(union1))
    return f"Union = {union_res} , Intersection = {inter_res} "

arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
print(union_intersection(arr1, arr2))