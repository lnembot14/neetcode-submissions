class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        1. Understand
            - core logic: Need a way to go and take the count of each character in 
            string and return True/False
            - input: two strings (s and t)
            - output: boolean

        2. Plan
            - create two dicitionaries one for each strings
            - take the count 
            - return comparison of dictionary

        3. Implement 

        '''

        s_dict = {}
        t_dict = {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1

        return s_dict == t_dict
        