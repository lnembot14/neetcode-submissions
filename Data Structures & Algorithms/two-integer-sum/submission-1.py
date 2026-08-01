class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tS_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in tS_dict:
                return [tS_dict[complement], i]
            tS_dict[nums[i]] = i
        