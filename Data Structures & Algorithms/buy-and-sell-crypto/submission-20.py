class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. Understand
            - core logic: Iterating through list, and subtracting values at indices
            to determine which value is the highest in terms of profit (max)
            - input: list of integers
            - output: integer
            - edge cases: empty list, list of one element, list of all the same 
            values 

        2. Plan 
            - initialize a set
            - find the minimum value in list
            - some type of check for where the value is located on set
            - compare values subtracted by minimum value to find the maximum
            return maximum

        3. Implement
        '''

        left = 0
        right = 1
        max_value = 0

        while right <= len(prices)-1:
            if prices[left] >= prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_value = max(profit, max_value)
            right += 1
        return max_value



        