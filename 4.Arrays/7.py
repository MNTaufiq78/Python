def insert_element(arr, value, position):
    new_arr = []
    for i in range(len(arr) + 1):
        if i < position:
            new_arr.append(arr[i])
        elif i == position:
            new_arr.append(value)
        else:
            new_arr.append(arr[i - 1])
    return new_arr

print(insert_element([10, 20, 30], 15, 1)) 
