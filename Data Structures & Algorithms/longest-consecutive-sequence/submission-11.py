class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        1. Understand
            - core logic: Going through list of nums starting with a value and 
            finding the largest sequence of numbers (1,2,3,4 etc)
            - input: list of integers
            - output: an integer
            - edge cases: empty list, list size of 1, all values in list have the 
            same integer

        2. Plan
            - declare a set for nums
            - declare max variable
            - loop through the set
            - check if num + 1 is in set
            - if it is create new variable called count and set it equal to 1
            - check while num + count is in set
                - increment count by 1
            - return max at end of loop

        3. Implement
        '''

        new_set = set(nums)
        max_count = 0

        for num in new_set:
            if num-1 not in new_set:
                count = 1
                while num + count in new_set:
                    count += 1
                max_count = max(count, max_count)
        return max_count
