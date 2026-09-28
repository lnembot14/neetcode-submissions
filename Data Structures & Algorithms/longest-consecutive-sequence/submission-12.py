class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        1. Understand
            - core logic: you create a set or a seperate data structure where
            you start off with each element in the list, if that number + 1 is 
            in the nums you increment the count and you end when there's no 
            longer a match
            - input: list of nums
            - output: integer
            - edge cases: empty list, list with duplicate values

        2. Plan
            - put all the values from nums in some type of set
            - try a for loop through the nums set and 

        3. Implement 
        '''

        new_set = set(nums)
        length = 0
        max_length = 0


        for num in new_set:
            if num - 1 not in new_set:
                length = 1 
                while num + 1 in new_set:
                    length += 1
                    num += 1
            max_length = max(length, max_length)
        return max_length