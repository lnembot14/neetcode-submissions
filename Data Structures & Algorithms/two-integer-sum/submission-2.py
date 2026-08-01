class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keep_dict = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in keep_dict:
                return [keep_dict[complement], i]
            keep_dict[nums[i]] = i
        