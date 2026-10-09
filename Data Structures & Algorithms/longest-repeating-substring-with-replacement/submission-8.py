class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. Understand
            - core logic: taking the longest substring of the string where 
            there are repeating characters via a replacement of a charcater 
            - input: string
            - output: integer 
            - edge cases: empty string, all characters are the same

        2. Match
            - dictionary needed for this problem, sliding window
            - window_len - most frequent element in string

        3. Plan
            - declare left pointer and max_length
            - loop with right pointer (for loop)
            - based on the character add it onto the dictionary
            - while loop to check when window_len - most frequent element is 
            not less than k
            - shrink the substring and decrement the count in dictionary
            - take the max_length of the window
            - return max_length

        4. Implement
        '''

        left = 0
        max_length = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            while ((right - left) + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, ((right-left) + 1))
        return max_length

        