class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. Understand (input/output, edge cases)
            - input: a list and a target
            - output: return an index from an element in the list if target is found
            edge cases:
                - empty list
                - two elements to search between

        2. Plan
            - intialize a pointer and an average variable
            - loop through the list
            - if target is found, return index of target
            - if not and still searching increment pointer and change average
            - if end of loop and can't find target return -1 

        3. Implement
        '''
        left = 0
        right = len(nums) - 1

        if len(nums) == 0:
            return -1 

        while left <= right:
            mid = (left + right) //2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1 



