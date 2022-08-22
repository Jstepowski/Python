from requests import head


def two_sum(nums, target):
    val_index_map = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in val_index_map:
            return [i, val_index_map[temp]]
        else:
            val_index_map[nums[i]] = i
    
def valid_parenthesis(s):
    bracket_map = {
        "}": "{",
        "]" : "[",
        ")" : "("
    }
    stack = []

    for char in s:
        if char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop(char)
            else:
                return False
        else:
            stack.append(char)
    
    if not stack:
        return True
    else:
        return False


def best_time_buy_and_sell(prices):
    l = 0
    r = 1
    max_profit = 0

    while r != len(prices):
        if r > l:
            temp = max(max_profit, prices[r] - prices[l])
        else:
            l = r
        r +=1

    return temp

def reverse_linked_list():
    prev = None
    curr = head

    while curr:
        head = curr.next
        curr.next = prev
        prev = curr
        curr = head

    return prev



def is_palindrome(s):
    new_str = ""

    for char in s:
        if char.isalnum():
            new_str += char.lower()
    if new_str == new_str[::-1]:
        return True
    else:
        return False

def merge_two_sorted(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1

    elif list2:
        tail.next = list2

    return dummy.next
    
        

def invert_binary_tree(root):
    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.right= temp

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

def max_depth_tree(root):
    if not root:
        return 0
    
    return 1 + max(self.max_depth_tree(root.left), self.max_depth_tree(root.right))


print(two_sum([1,3,7,2], 5))

print (valid_parenthesis("[}}]"))