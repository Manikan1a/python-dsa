class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        highest_profit=0
        for i in range(1,len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]
            else:
                profit=prices[i]-lowest
                if profit>highest_profit:
                    highest_profit=profit
        return highest_profit
