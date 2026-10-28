class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Understand
            - core logic: as you go through the list of strings, your grouping 
            them together by whether or not they are the same anagram or not
            - input: list of strings 
            - output: list of a list (2d list)
            - edge cases: empty list,

        2. Plan
            - initialize the group dictionary
            - loop through the list of strs
            - sort word based on order (variable for that)
            - check whether or not that sorted word is already in the dictionary
                - if it is, add it on as a initial element in list
                - if it isn't append it to the already created list
            - return list of values 


        3. Implement
        '''
        
        group_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in group_dict:
                group_dict[sorted_word] = [word]
            else:
                group_dict[sorted_word].append(word)
        return list(group_dict.values())