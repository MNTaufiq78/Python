def starts_with(s, prefix):
    for i in range(len(prefix)):
        if i >= len(s) or s[i] != prefix[i]:
            return False
    return True

def ends_with(s, suffix):
    suffix_len = len(suffix)
    s_len = len(s)
    for i in range(suffix_len):
        if s[s_len - suffix_len + i] != suffix[i]:
            return False
    return True

print(starts_with("hello", "he"))  
print(ends_with("hello", "lo"))  
