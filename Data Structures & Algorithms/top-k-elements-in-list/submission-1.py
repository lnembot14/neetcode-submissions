class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ For this problem, Im inputing an array (nums) and an int(
        k) that represents the elements of the array that show up the kth times)"""
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) + 1
        sorted_keys = sorted(my_dict, key=lambda x: my_dict[x], reverse=True)
        return sorted_keys[:k]
        