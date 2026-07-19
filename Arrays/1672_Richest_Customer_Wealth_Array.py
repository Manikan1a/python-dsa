class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for i in range(len(accounts)):
            current_wealth=0
            for j in range(len(accounts[i])):
                current_wealth+=accounts[i][j]
            wealth.append(current_wealth)
        return max(wealth)
