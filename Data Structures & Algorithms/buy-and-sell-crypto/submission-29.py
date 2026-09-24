class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        profit = 0

        while right <= len(prices)-1:
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            right += 1 
            max_profit = max(profit, max_profit)
        return max_profit
        