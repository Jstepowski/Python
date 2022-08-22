def contains_duplicates(l):
    values = []
    for num in l:
        if num in values:
            return True
        else:
            values.append(num)
    return False

dups = []
l = ["dup", "dup", "cat", "dog", "dog"]
print(contains_duplicates(l))   
