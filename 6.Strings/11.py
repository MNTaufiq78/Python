def split_string(s, delimiter):
    result = []
    temp = ""
    for ch in s:
        if ch == delimiter:
            result.append(temp)
            temp = ""
        else:
            temp += ch
    result.append(temp)
    return result

print(split_string("hello,world,python", ','))  
