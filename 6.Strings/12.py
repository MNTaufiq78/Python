def int_to_string(n):
    result = ""
    is_negative = False
    
    if n == 0:
        return "0"
    
    if n < 0:
        is_negative = True
        n = -n
    
    while n > 0:
        digit = n % 10
        result = chr(digit + 48) + result 
        n = n // 10
    
    if is_negative:
        result = "-" + result
    
    return result

print(int_to_string(123)) 
print(int_to_string(-456))  
