def difference_max_min(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return max_val - min_val

print(difference_max_min([1, 2, 3, 10]))  
