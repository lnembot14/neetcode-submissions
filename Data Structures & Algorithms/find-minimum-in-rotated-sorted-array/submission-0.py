class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. Understand
            - core logic: using binary search on a rotated array and having
            to find the minimum value
            - input: list of integers
            - output: single integer
            - edge cases: empty list

        2. Plan
            - find the minimum element in nums
            - perform binary search to check said value 

        3. Implement 
        '''
        min_val = nums[0]
        for i in range(len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
        return min_val
        
        