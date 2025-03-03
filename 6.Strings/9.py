def trim_string(s):
    start = 0
    end = len(s) - 1

    while start <= end and s[start] == ' ':
        start += 1

    while end >= start and s[end] == ' ':
        end -= 1

    result = ""
    for i in range(start, end + 1):
        result += s[i]
    
    return result

print(trim_string("  hello world  ")) 
