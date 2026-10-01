class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. Understand
            - core logic: trying to find the max profit between buying and selling
            a stock, we know that the day to buy pointer must be less than the day
            to sell pointer. 
            - input: list of integers 
            - output: integer value
            - edge cases: empty list, sorted element list

        2. Plan
            - set your left and right pointer
            - set up profit and max profit pointers
            - while loop to check whether the right pointer has reached the end
            - if the left pointer is greater than the right pointer, change the 
            location to where the right pointer is
            - estimate the profit and store it in max_profit
            - return max_profit

        3. Implement 
        '''

        left = 0
        right = 1
        profit = 0
        max_profit = 0

        while right <= len(prices) -1 :
            if prices[left]>prices[right]:
                left = right
            profit = prices[right] - prices[left]
            right += 1
            max_profit = max(profit, max_profit)
        return max_profit
        