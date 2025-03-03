def find_index(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1 

print(find_index("Hello", 'l'))  
