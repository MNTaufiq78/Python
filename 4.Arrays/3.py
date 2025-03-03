def find_index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

print(find_index([10, 20, 30, 40], 30)) 
