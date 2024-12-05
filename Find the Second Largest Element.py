def second_largest(arr):
    if len(arr) < 2:
        return None
    unique_elements = list(set(arr))
    unique_elements.sort(reverse=True)
    return unique_elements[1] if len(unique_elements) > 1 else None

# Test
print(second_largest([10, 20, 20, 4, 45, 99]))  # 45
