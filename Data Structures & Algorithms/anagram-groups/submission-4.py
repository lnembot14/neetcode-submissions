class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Understand
            - core logic: Your taking a list of strings and returning a list of
            lists that contains the same exact characters, so your categorizing them 
            based on the strings that your given
            - input: list of strings 
            - output: list of list of strings 
            - edge cases: all the strings in the list contain the same word, empty
            list, list of empty strings 

        2. Plan
            - declare a dictionary for all the values to go inside of
            - loop through list
            - you want to check whether the strings is already in the anagram list
                - if so you create a new list with said value
                - if not, you append that value onto the dictionary list
            - return the dictionary values in a list. 

        3. Implement
        '''

        anagram_dict = {}

        for word in strs:
            ordered_word = "".join(sorted(word))
            if ordered_word not in anagram_dict:
                anagram_dict[ordered_word] = [word]
            else:
                anagram_dict[ordered_word].append(word)  
        return list(anagram_dict.values())