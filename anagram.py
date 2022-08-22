def isAnagram(s, t):
    nums_s = {}
    nums_t = {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        nums_s[s[i]] = 1 + nums_s.get(s[i], 0)
        nums_t[t[i]] = 1 + nums_t.get(t[i], 0)
    
    for k in nums_s:
        if nums_s[k] != nums_t.get(k, 0):
            return False

    return True

