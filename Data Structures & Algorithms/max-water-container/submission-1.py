class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        1. Understand
            - input: list of integers
            - output: max area (integer)
            - core logic: two pointers, measure the area there and keep going until 
            you get an updated value 
            - edge cases: empty list, all the values in list are unable to make a 
            container, elements of list are the same integer

        2. Plan
            - declare a left and right pointer
            - declare max variable
            - loop through list
            - find area for each stretch and compare the left pointer to right
            - if left smaller than right set left = right


        3. Implement 
        '''



        left = 0
        right = len(heights) -1
        max_area = 0
        area = 0

        while left < right:
            area = ((right - left) * min(heights[left], heights[right]))
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]: 
                right -= 1
            max_area = max(area, max_area)
        return max_area
            
            
                
        