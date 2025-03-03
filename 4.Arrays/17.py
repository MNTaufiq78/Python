def contains_12_23(arr):
    found_12 = False
    found_23 = False
    for num in arr:
        if num == 12:
            found_12 = True
        if num == 23:
            found_23 = True
    return found_12 and found_23

print(contains_12_23([10, 12, 23, 34]))  