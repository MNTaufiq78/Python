def count_even_odd(arr):
    evens = 0
    odds = 0
    for num in arr:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

print(count_even_odd([1, 2, 3, 4, 5, 6]))  
