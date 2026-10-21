class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. Understand
            - core logic: going through the integers of the list and finding the max
            profit between different days 
            - input: a list of integers 
            - output: integer
            - edge cases: empty list, duplicate values of profit

        2. Plan
            - declare my left and right pointer
            - declare profit and max_profit
            - loop through the list with the right pointer (for loop)
                - condition to check whether the left pointer is greater 
                than the right 
                - if so, set the left pointer to where the right is 
                - if not keep stretching out the right pointer and taking the profit
                - profit = profit[right] - profit[left]
            - use max profit and update at each iteration
            - return max_prodit 

        3. Implement
        '''

        left = 0
        profit = 0
        max_profit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        return max_profit
        