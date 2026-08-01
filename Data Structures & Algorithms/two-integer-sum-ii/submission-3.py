class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1. Understand
        - input: list and target value 
        - output: a list of the indexes where the addition adds up
        - core logic: find a way to go through each element using a pointer at the
        beginning and end, based on whether or not they are equal, continue to move that
        pointer
        - edge cases: target not found in list, numbers don't add up to target

        2. Plan
        - declare left and right pointers
        - while left < right
        - you'd add the pointers together, if the value is less than target 
        move the left pointer up, if the value is greater than the target move
        the right pointer down
        once you find that it equals target, you want to return a list with the 
        indexes + 1 

        3. Implement
        '''
        
        index1 = 0
        index2 = len(numbers)-1

        while index1 <= index2:
            if numbers[index1] + numbers[index2] > target:
                index2 -= 1 
            elif numbers[index1] + numbers[index2] < target:
                index1 += 1
            else:
                return [index1+1, index2+1]


            