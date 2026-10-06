class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand
            - core logic: go through the string and identify each character, if 
            character has not yet been seen, continue, if so stop and begin with new
            string 
            - input: string 
            - output: integer 
            - edge cases: empty string, entire string doesn't contain any duplicates

        2. Plan
            - create a new string
            - initialize left and right pointer at respetive characters
            - loop until you reach the end of string 
            - keep updating the new string
            - return max_length

        3. Implement
        '''
        charSet = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_length = max(max_length, len(charSet))
        return max_length

