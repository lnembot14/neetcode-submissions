class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        1. Understand (input/output, edge cases)
            - For the input we're given a list of strings 
            - for the output we need to return the same a 2d list where each element 
            is a group of words that have the same anagram
            - anagram: words that contain the same letters
            
            edge cases:
            - Empty list, 
            - lowercase and uppercase letters
            - string might have an integer in there 

        2. Plan
            - declare dictionary
            - loop through list
            - create a variable that represents each potential anagram
            - check if the string that we've seen is in the anagram dicitonary
            - if word is in the list, we append it
            - if not we create a new list for that anagram representation
            - after return the values from dicitonary in list form

        3. Implement
        '''

        my_dict = {}

        for word in strs:
            anagram_representation = str(sorted(word.lower()))

            if anagram_representation not in my_dict:
                my_dict[anagram_representation] = [word]
            else:
                my_dict[anagram_representation].append(word)

        return list(my_dict.values())

        