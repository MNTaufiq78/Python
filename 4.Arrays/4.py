def contains_value(arr, value):
    for num in arr:
        if num == value:
            return True
    return False

print(contains_value([1, 2, 3, 4], 3))  
