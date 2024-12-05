def max_product_subarray(arr):
    max_prod = min_prod = result = arr[0]
    for num in arr[1:]:
        temp_max = max(num, max_prod * num, min_prod * num)
        min_prod = min(num, max_prod * num, min_prod * num)
        max_prod = temp_max
        result = max(result, max_prod)
    return result

print(max_product_subarray([2, 3, -2, 4]))  # 6
