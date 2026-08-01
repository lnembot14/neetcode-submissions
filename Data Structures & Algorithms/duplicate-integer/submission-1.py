class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}

        for num in nums:
            if num not in dup_dict:
                dup_dict[num] = 1
            else:
                dup_dict[num] += 1
        for value in dup_dict.values():
            if value > 1:
                return True
        return False 
        