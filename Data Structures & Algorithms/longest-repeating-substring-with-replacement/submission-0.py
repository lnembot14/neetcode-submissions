class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. Understand
            - core logic: Go through string, determine k look at second letter,
            try and keep track of the longest streak you can keep with the replaced
            letter
            - input: string of all uppercase letters
            - output: integer of max length of repeating characters
            - edge cases: lowercase letters involved, non alphanumeric charcaters,
            empty string

        2. Plan
            - declare max length variable and counter variable
            - iterate through the string, check if the next string is equal to the
            previous
                - if it is increase max amount and keep iterating
                - if not increment counter variable and keep iterating until counter
                is equal to k 
            return max variable

        3. Implement
        '''
        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            while (right-left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left+=1
            res = max(res, right-left+1 )
        return res

        
            

            



        