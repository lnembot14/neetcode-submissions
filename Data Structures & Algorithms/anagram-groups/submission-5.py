class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Understand
            - core logic: go through list and determine the specific anagrams and   
            whether said string is apart of a group of anagrams or its own
            - input: list of strings 
            - output: list of list of strings with ordered anagrams (dictionary)
            - edge cases: empty list, all unique strings, lists of one element

        2. Plan
            - create a dictionary to keep track of all the potential anagrams
            - loop through the input list
            - determine whether that string ordered is already in the dictionary
                - if it is add it on to the dictionary as a list
                - if not, create a new list starting with said string
            - return list of values in dictionary 

        3. Implement
        '''

        anagram_dict = {}

        for word in strs:
            anagram_word = "".join(sorted(word))
            if anagram_word not in anagram_dict:
                anagram_dict[anagram_word] = [word]
            else:
                anagram_dict[anagram_word].append(word)
        return list(anagram_dict.values())
        