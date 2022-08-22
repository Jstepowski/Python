def return_max_profit(prices):
    global_max = 0
    left_ptr = 0
    right_ptr = 1
    while right_ptr < len(prices):
        if prices[left_ptr] < prices[right_ptr]:
            profit = prices[right_ptr] - prices[left_ptr]
            if profit > global_max:
                global_max = profit
        else:
            left_ptr = right_ptr
        right_ptr +=1
    return global_max

prices = [7, 1, 5, 4, 6, 3]
print (return_max_profit(prices))
