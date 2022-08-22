def valid_parenth(s):
    stack = []

    parenth_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
    }

    for char in s:
        print (stack)
        if char in parenth_map:
            print (char)
            if stack and stack[-1] == parenth_map[char]:
                stack.pop()
                print(stack)
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


test_str1 = "{[()]}"

print(valid_parenth(test_str1))