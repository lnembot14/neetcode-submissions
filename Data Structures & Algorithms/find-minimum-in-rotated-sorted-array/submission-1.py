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
        res = nums[0]
        left = 0
        right = len(nums) - 1
    

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] >= res:
                left = mid + 1
            else:
                right = mid - 1
            res = min(res, nums[mid])
        return res


        
        
        