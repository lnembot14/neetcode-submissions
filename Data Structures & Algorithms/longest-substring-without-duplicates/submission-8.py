class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        slow_pointer = 0
        fast_pointer = 1
        substring = s[slow_pointer]
        max_length = 0

        while fast_pointer < len(s):
            if s[fast_pointer] in substring:
                max_length = max(max_length, len(substring))
                substring = substring[1:]
                slow_pointer +=1 
            else:
                substring += s[fast_pointer]
                fast_pointer +=1 
        max_length = max(max_length, len(substring))
        return max_length 