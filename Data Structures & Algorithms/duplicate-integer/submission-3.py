class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        1. Understand 
            - go through list and check if any of the values in the list are 
            repeated
            - input: list of integers
            - output: boolean
            - edge case: empty list, list with one element, list with more than one
            duplicate value

        2. Plan
            - declare a new set
            - loop through list
            - add values to set based on whether or not they've been seen
                - if value is already in list: return fals
            - outside of loop return True

        3. Implement 
        '''

        nums_set = set()

        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return True
        return False
        