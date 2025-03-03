def copy_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr

original = [1, 2, 3]
copied = copy_array(original)
print(copied)  
