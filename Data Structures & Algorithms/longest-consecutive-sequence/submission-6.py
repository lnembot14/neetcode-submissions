class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        1. Understand 
            - core logic: going through each numbered element in list and figuring
            out whether said value contains an element that is +1 from it.
            If it's not then you start a new count, if you start a new count and 
            there isn't, you end the count
            - input: list of integers
            - output: integer
            - edge cases: empty list, each element in list is the same number. 

        2. Plan
            - declare set variable
            - loop through the list, then check whether that value -1 is in the list
            - if it's not, start the new count 
                - while num + count is still equal to a value in the set, keep  
                incrementing the count
            - return max_length once the consecutive streak is over

        3. Implement 

        '''

        new_set = set(nums)
        max_length = 0
        
        for num in nums:
            if num - 1 not in new_set:
                count = 1
                while num + count in new_set:
                    count += 1
                max_length = max(max_length, count)
        return max_length
        