def average_array(arr):
    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    return total / count if count > 0 else 0

print(average_array([1, 2, 3, 4, 5])) 
