def is_alpha(s):
    for ch in s:
        if not ('A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
            return False
    return True

print(is_alpha("Hello"))  
print(is_alpha("Hello123")) 
