def main(prices):
    buyPrice = prices[0]
    maxProfit = 0

    for price in prices[1:]:
        if price < buyPrice:
            buyPrice = price
    
        maxProfit = max(maxProfit, price - buyPrice)
    
    print(maxProfit)
        

main([1,2])