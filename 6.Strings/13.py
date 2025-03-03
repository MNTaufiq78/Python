def to_uppercase(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)  
        else:
            result += ch
    return result

def to_lowercase(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32) 
        else:
            result += ch
    return result

print(to_uppercase("hello"))  
print(to_lowercase("WORLD"))  
