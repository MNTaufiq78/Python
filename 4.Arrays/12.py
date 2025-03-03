def remove_duplicates(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr

print(remove_duplicates([1, 2, 2, 3, 4, 4])) 