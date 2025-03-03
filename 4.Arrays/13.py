def second_largest(arr):
    max_val = arr[0]
    second_max = None
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif second_max is None or (num > second_max and num != max_val):
            second_max = num
    return second_max

print(second_largest([10, 20, 4, 45, 99]))  
