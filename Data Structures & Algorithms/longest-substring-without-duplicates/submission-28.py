class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand
            - core logic: creating a substring and keeping track of how many 
            characters it can go by without hitting a duplicate
            - input: string 
            - output: integer
            - edge cases: empty string, whole string contains no duplicates, string
            is just duplicates

        2. Plan
            - declare left and right pointers
            - declare max_length
            - declare substring variable
            - iterate through the list with pointer, if word is not in substring,
            add character to substring variable
                - if word in substring, move left pointer to where right is and
                begin again (slicing)
            return max_variable

        3. Implement
        '''

        left = 0
        charSet = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_length = max(max_length, len(charSet))
        return max_length
