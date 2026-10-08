class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Understand
            - core logic: essentially going through each character and determining
            where the longest subsrting occurs (no repeating characters)
            - input: string
            - output: integer
            - edge cases: empty string, every string is a non repeated character 

        2. Plan
            - initialize our set
            - use left and right pointers
            - use the right pointer to loop through the list
            - use a while loop to remove the left most element (most likely the 
            duplicate)
            - append the value onto the set
            - take the maximum of the length of the set
            - return maximum 

        3. Implement 
        '''

        charSet = set()
        left = 0
        max_length = 0


        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_length = max(max_length, len(charSet))
        return max_length
        