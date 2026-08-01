class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Input - array of elements(integers)
        Output - Boolean
        Based on array or list inputted, I must return a boolean to examine
        whether an array contains a duplicate
        """
        sorted_nums = set()
        for num in nums:
            if num in sorted_nums:
                return True
            sorted_nums.add(num)
        return False              
        