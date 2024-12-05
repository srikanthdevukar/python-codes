def stable_even_odd(arr):
    even_index = 0     
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_number = arr[i]             
            for j in range(i, even_index, -1):
                arr[j] = arr[j - 1]            
            arr[even_index] = even_number            
            even_index += 1  
    return arr
arr = [7, 6, 2, 4, 9, 11, 3, 8]
result = stable_even_odd(arr)
print(result)
