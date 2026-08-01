class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand 
            - input: given a string of characters
            - output: must return an integer 
            - logic: you take a string and count the amount of times that an occuring string 
            doesn't appear, eventually you loop through the whole list and check 
            - edge cases: all the characters are the same, empty string, entire stirng doesn't contain 
            duplicates

        2. Plan
            - declare variables: max_length, right and left pointers and set
            - double while loop: one to check while the right hasn't reached the end
            and another to check while a current value that needs to be removed is still in the 
            set
            - for the first check, you want to move the right pointer and add it onto the set
            - if not you're moving the left pointer and removing that value from the set, to avoid duplicates
            - update the max_length variable
            - return max_length

        3. Implement 
        '''

        max_length = 0
        right = 0
        left = 0
        dup_set = set()

        if len(s) == 0:
            return 0

        while right <= len(s)-1:
            while s[right] in dup_set:
                dup_set.remove(s[left])
                left += 1      
            dup_set.add(s[right])
            right += 1
            max_length = max(max_length, len(dup_set))
        return max_length
        