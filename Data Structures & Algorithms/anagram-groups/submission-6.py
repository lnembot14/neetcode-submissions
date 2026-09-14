class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}

        for word in strs:
            ordered_word = "".join(sorted(list(word)))
            if ordered_word not in group_dict:
                group_dict[ordered_word] = [word]
            else:
                group_dict[ordered_word].append(word)
        return list(group_dict.values())
        