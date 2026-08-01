class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand (input/output, edge cases, tradeoffs)
            - Taking a string and returning the maximum amount of times that letters 
            in it are not the same (substring without repeating characters)
            - empty string
            - all strings are the same letter


        2. Plan 
            -Initialize fast and slow pointers
            - also intialize the max length variable and seen substring
            - iterate with a while loop until the fast pointer is at the end of string
            - increment fast pointer and add it to seen substring if character is not already in seen
            - if letter is seen, increment slow pointer and use slice to cut substring


        3. Implement 
        '''

        if len(s) == 0:
            return 0

        slow_pointer = 0
        fast_pointer = 1
        seen = s[slow_pointer]
        max_length = 0

        while fast_pointer < len(s):
            if s[fast_pointer] in seen:
                max_length = max(max_length, len(seen))
                seen = seen[seen.index(s[fast_pointer])+1:]
                slow_pointer += 1
            else:
                seen += s[fast_pointer]
                fast_pointer +=1 
        max_length = max(max_length, len(seen))
        return max_length
        