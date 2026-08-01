class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        1. Understand (input/output, run time, edge cases)
            - Looking through a linked list/list and identifying where duplicate is
            - need to return duplicate number
            - each integer is in in the range [1,n] meaning that there are cycles
            - O(1) extra space
            - No modifying of array
            - empty array

        2. Plan
            - initiailze two pointers slow and fast (set to 0 at first)
            - Phase(1) - use a while loop to iterate through the list, moving fast twice and slow once
            until values meet (somewhere in the cycle)
            - set slow back to 0
            - phase (2) - use a while loop to iterate through the list, this time moving both pointers by 
            one until they meet (this would represent the duplicate)
            - return one of pointers


        3. Implement 
        '''

        if len(nums) == 0:
            return 0
            
        slow = 0
        fast = 0

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
        