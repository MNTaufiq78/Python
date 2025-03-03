def remove_element(arr, value):
    new_arr = []
    for num in arr:
        if num != value:
            new_arr.append(num)
    return new_arr

print(remove_element([1, 2, 3, 4, 3], 3))  