class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        1. Understand
            - input: list of integers
            - output: an integer of the longest consecutive streak between integers
            in list 
            - core logic: making a new list/set and going through each element in the list
            to see if it's value -1 is in the list 
            - edge cases: Only one element in the list, empty list or list contains
            all of the same element 

        2. Plan
            - declare a set or list
            - iterate through each element in the list
                - check if the element-1 is in our set if not, make a new list starting
                with that element
                    continuing on with that list check if the next element -1 is equal to the value + 1
                    if so add that on to list 
                    if not create a variable max length and set
                    it equal to the length of said value and start again
                return value 

        3. Implement 
        '''

        new_set = set(nums)
        max_length = 0

        for num in new_set:
            if num -1 not in new_set:
                count = 1
                while num + count in new_set:
                    count += 1
                max_length = max(max_length, count)
        return max_length



        