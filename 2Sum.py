
def two_sum(nums, target):
    hash_map = {}
    
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in hash_map:
            return [i, hash_map[temp]]
        else:
            hash_map[nums[i]]= i
    return False


def valid_parenthesis(s):
        m_ap = {")" : "(",
                "]" : "[",
                "}" : "{"
               }
        
        stack = []

        for char in s:
            if char in m_ap:
                if stack and stack[-1] == m_ap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False
                

def best_time_buy_and_sell(prices):

    i = 0
    j = 1
    max_p =0

    while j != len(prices):
        if prices[j] > prices[i]:
            local_p = prices[j] - prices[i]
            max_p = max(local_p, max_p)
        else:
            i = j
        j +=1
    return max_p


nums = [1 ,7, 3, 11]
target = 10

#print(two_sum(nums, target))


# s = "[({})]"
# print(valid_parenthesis(s))

prices = [7,1,5,3,6,4]
print(best_time_buy_and_sell(prices))

