def remove_duplicates_new_array(arr):
    new_arr = []
    for num in arr:
        found = False
        for n in new_arr:
            if n == num:
                found = True
                break
        if not found:
            new_arr.append(num)
    return new_arr

print(remove_duplicates_new_array([1, 2, 2, 3, 4, 4]))  