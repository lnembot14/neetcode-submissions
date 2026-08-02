class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Understand
            - core logic: keeping track of each integer in list and essentiall
            it's count then taking the top k ones (maybe some slicing)
            - input: list of integers
            - output: list of top values
            - edge cases: empty list, the number of elements within the list is less
            than k

        2. Plan
            - declare a dictionary
            - take the count of each element into said dictionary
            - 

        3. Implement

        '''

        nums_dict = {}

        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1 

        new_list = []

        ordered_nums = dict(sorted(nums_dict.items(), reverse=True, key=lambda
        item:item[1]))

        for num in ordered_nums:
            new_list.append(num)

        return new_list[:k]
            

        