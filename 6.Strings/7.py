def compare_strings(s1, s2):
    if s1 == s2:
        return 0  
    elif s1 > s2:
        return 1  
    else:
        return -1  

print(compare_strings("apple", "banana"))  
print(compare_strings("mango", "apple"))  
print(compare_strings("hello", "hello"))  
