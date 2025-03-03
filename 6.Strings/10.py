def replace_char(s, old, new):
    result = ""
    for ch in s:
        if ch == old:
            result += new
        else:
            result += ch
    return result

print(replace_char("hello", 'l', 'x'))  
