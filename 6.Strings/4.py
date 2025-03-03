def substring(s, start, end):
    result = ""
    for i in range(start, end):
        result += s[i]
    return result

print(substring("HelloWorld", 0, 5))  
