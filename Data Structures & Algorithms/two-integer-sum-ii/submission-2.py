class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1. Understand (core logic, input, output, edge cases)
            - input: numbers and a target integer
            - output: a list of indexes (index 1 must be less than index 2)
            - edge cases: target not found, empty list, unsorted list
            string in one of the list elements, negative integers

        2. Match
            - checking index1 and index2 (tells me that this must be a two poin
            ter type of problem)
            - similar to two sum (two sum involved a complement and dictionary
            but the same idea is here)
            - going to need to declare two pointers at different locations of the 
            list and keep comparing the products until the right answer is found

        3. Plan
            - declare left and right pointers
            - loop while left is less than right
            - compare the the value from the left pointer and right pointer to see if index1 is
            less than index2
            - if that value is not equal to the target, move the right pointer down 1 
            - continue looping until the sum of index1 and index2 is equal to target and 
            return list 

        4. Implement

        5. Review 

        6. Evaluate
        '''
        left = 0
        right = len(numbers) -1 

        if len(numbers) == 0:
            return 0

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
                

        