class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. Understand
            - core logic:
            - input: string
            - output: integer (length of longest substring)
            - edge cases: empty string, k could be 0, characters of string
            are all the same 

        2. Plan
            - create a dictionary to keep track of each character relative to
            the length of the string 

        3. Implement
        '''

        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while ((right-left) + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, (right - left) + 1)
        return max_length
            


            

        
        