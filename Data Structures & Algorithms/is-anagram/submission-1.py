class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        1. Understand 
        - comparing two strings and check if they can be anagrams of each other 
        - edge cases: length of one string is shorter than the other, empty string, 
        - input: two strings
        - output: boolean


        2. Plan 
        - make a dictionary for each string
        - loop through each string and add letters and count
        - compare dicitionaries in return statement 


        3. Implement 
        '''

        s_dict = {}
        t_dict = {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
            
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        
        return t_dict == s_dict
        