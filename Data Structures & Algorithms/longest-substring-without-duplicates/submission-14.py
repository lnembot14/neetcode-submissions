class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand
            - Input: Taking in a string of n characters
            - output: returning an integer
            - edge cases: every character is the same character, capitalized and 
            lowercased letters
            -Logic: create a set that goes through each character and returns the largest 
            from each


        2. Plan
            - initialize left and right pointers
            - initialize set
            - loop through string
            - conditional to check if the character hasn't seen yet. If so, 



        3. Implement

        '''

        left = 0
        right = 0
        longest_substring = set()
        max_length = 0
        

        if len(s) == 0:
            return 0


        while right <= len(s) -1 :
            while s[right] in longest_substring:
                longest_substring.remove(s[left])
                left += 1
            longest_substring.add(s[right])
            max_length = max(max_length, len(longest_substring)) 
            right += 1
        
        return max_length

        