class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. Understand
            - core logic: initialize your left and right pointers at the beginning
            of the algorithm and you want keep moving them on a condition where you
            find the largest area. min(heights[left], heights[right]) * distance of
            heights 
            - input: list of integer values
            - output: output number
            - edge cases: empty list

        2. Plan
            - set your left and right pointers, as well as your max_area variable


        3. Implement 
        '''

        left = 0
        right = len(heights) - 1
        max_area = 0
        area = 0

        while left <= right:
            area = min(heights[left], heights[right]) * (right - left) 
            max_area = max(area, max_area)
            if heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1
        return max_area
            
        