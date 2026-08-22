class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set()

        for num in nums:
            if num not in check_set:
                check_set.add(num)
            else:
                return True
        return False