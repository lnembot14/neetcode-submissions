class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Understand (input/output, edge cases)
            - Inputting a list of integers, sliding from left pointer to k to find
            the maximum values within window section.
            -return an array of those max values 
            - Need to use deque to remove elements from both the left and right side
            - edge cases, sliding window that is less than k, empty list, list with less than k integers


        2. Plan 
            - declare deque, right and left pointers then result array
            - loop while right is less than the nums list
            - loop to check whether the value on the right most side is less than the 
            value we're entering into the deque, if so remove that element before appending the new one
            - also check if the left most element is out of bounds when it comes to the left most element of 
            the deque if so, remove that element from the queue and move
            - one more conditional to check whether the sliding window is in the appropriate position, 
            we move the left pointer and add the element to the result array and continue to increment 
            the right pointer 
            - return result array

        3. Implement 
        '''

        right = 0
        left = 0
        max_array = []
        dq = collections.deque()

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right] :
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()

            if (right + 1) >= k:
                max_array.append(nums[dq[0]])
                left += 1
            right += 1
        return max_array

        