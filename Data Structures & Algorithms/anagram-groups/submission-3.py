class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Understand
            - core logic: The core logic for this problem is using a variable that sorts each
            string then for each string in the list, if that string sorted is equal to the 
            sorted version, add it on to the list of the dictionary
            - input: list of strings
            - output: list of lists containing strings
            - edge cases:  empty string, all letters sorted are the same anagram, 
            one of the strings contains an integer (harder to sort )

        2. Plan
            - initialize dictionary that will contain group anagrams
            - loop through list, and use a variable to declare a sorted string
            - check if string is already in dictionary
                - if not declare the list with that string
                - if so append value onto dictionary

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
    
        