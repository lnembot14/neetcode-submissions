class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. Understand
            - core logic: You want to use two pointers, one at the beginning of the
            list and another at the end take the area of the two pointers and 
            declare it as the max area, keep moving pointers based on minimum value
            - input: list of integers
            - output: an integer of the area 
            - edge cases: empty list, list of size 1

        2. Plan
            - initialize left and right pointers
            - initialize result variable
            - iterate while left pointer is less than or equal to right pointer
            - take the area of the two indices (r-l) * min(height[r], height[l])
            - initially set equal to max area or result
            - compare left and right pointers, move the smaller value accordingly,
            - if you find a value greater than initial max area update
            - keep iterating until left and right at some position, then return result 

        3. Implement
        '''

        left = 0
        right = len(heights) -1 
        res = 0

        while left <= right:
            max_area = (right-left) * min(heights[right], heights[left])
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            elif heights[right] == heights[left]:
                left += 1
            res = max(max_area, res)
        return res
        