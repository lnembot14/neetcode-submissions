class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Understand (input/output, tradeoffs and edge cases)
            - Input: list of size n, and k representing an integer
            - k is important here, used to decide how long the second pointer should
            stretch
            - after each check both pointers should increment by one
            - output, a list containing the max integer from each slide
            - ends when the right pointer reaches the end of the list
            - empty array or any array size that's less than k 


        2. Plan 
            - Initialize a max_array
            - use a deque (double ended queue to remove max elements from the front and back of list)
            - initalize pointers one at the beginning of the list and the other also at the beginning of the list
            - loop while the right pointer is less than the length of the list
            - add elements onto deque, remove the ones that are less than the max
            - append max elements onto new array
            - return new array

        3. Implement 
        '''

        left = 0
        right = 0
        q = collections.deque()
        output = []

        while right < len(nums):

            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
                

            if (right+1) >= k:
                output.append(nums[q[0]])
                left += 1 
            right += 1 
        
        return output
        

        