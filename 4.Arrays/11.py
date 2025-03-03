def common_values(arr1, arr2):
    common = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common:
                common.append(num1)
    return common

print(common_values([1, 2, 3], [2, 3, 4]))  
