class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in my_dict:
                my_dict[sorted_word] = []
            my_dict[sorted_word].append(word)
        return list(my_dict.values())