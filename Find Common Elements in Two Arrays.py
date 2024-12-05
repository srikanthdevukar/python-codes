def find_common(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(find_common([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
