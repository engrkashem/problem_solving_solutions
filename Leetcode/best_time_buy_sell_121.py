class Solution(object):
    def maxProfit(self, prices):
        minPrice=prices[0]
        profit=0

        for price in prices:
            if price<minPrice:
                minPrice=price
            
            potentialProfit=price-minPrice

            if potentialProfit>profit:
                profit=potentialProfit
        
        return profit

        # for i,num1 in enumerate(prices, start=1):
           
        #     for j in range(i, len(prices)):
        #         num2=prices[j]

        #         if num2-num1 > profit:
        #             profit=num2-num1
            
        # return profit


obj= Solution()

# inp1=[7,1,5,3,6,4]
# inp1=[7,6,4,3,1]
inp1=[1,2]

print(obj.maxProfit(inp1))


from functools import reduce

def maxProfit(self, prices):
    if not prices:
        return 0

    return reduce(
        lambda acc, price: (
            min(acc[0], price),  # Update minPrice if the current price is lower
            max(acc[1], price - acc[0])  # Calculate potential profit and keep the maximum
        ),
        prices,
        (float('inf'), 0)  # Initial values: (minPrice, profit)
    )[1]  # The result is the second element (profit)

