
def get_profit(prices):
    l = 0
    r = 1
    profit = 0

    while r != len(prices):
        if prices[r] > prices[l]:
            local_profit = r - l
            profit =  max(local_profit, profit)
        else:
            l = r
        r +=1

    return profit

prices = [7,1,5,3,6,4]
prices_2 = [7,6,4,3,1]

print(get_profit(prices))