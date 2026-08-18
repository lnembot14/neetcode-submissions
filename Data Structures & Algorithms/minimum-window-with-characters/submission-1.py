class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        1. Understand
            - core logic: loop through s and compare to T then use slicing or
            building a new sttring to return the substring
            - input: two parameters, string s and t
            - output: string (substring of s)
            - edge cases: duplicate strings, length of string t greater than
            string s, contains numbers, 

        2. Plan
            - 

        3. Implement 
        '''

        if t == "":
            return ""
        
        window = {}
        t_dict = {}

        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        have = 0
        need = len(t_dict)
        min_substring = [-1, -1]
        min_len = float("infinity")

        left = 0
        for right in range(len(s)):
            c = s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1

            if c in t_dict and window[c] == t_dict[c]:
                have += 1

            while have == need:
                if (right - left + 1) < min_len:
                    min_substring = [left,right]
                    min_len = (right - left +1)
                window[s[left]] -= 1
                if s[left] in t_dict and window[s[left]] < t_dict[s[left]]:
                    have -=1
                left += 1

        left, right = min_substring
        return s[left: right+1] if min_substring != float("infinity") else ""



        


        
        