

# solution not caring about alpha, caps and not allowing s = s[::-1]


def is_palindrome(s):
    l = 0
    r = len(s)-1

    while l != r:
        if s[l] != s[r]:
            return False
        else:
            while (l<r):
                l +=1
            while (r>l):
                r -=1
    return True

words = ["redivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", "planet", "galaxy", "star", "icecream"]
for word in words:
    palindrome = is_palindrome(word)
    if palindrome:
        print(f" {word} is a palindrome")
    else:
        print(f" {word} is not a palindrome")


    


    
    