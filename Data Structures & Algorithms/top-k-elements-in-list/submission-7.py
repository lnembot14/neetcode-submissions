class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Understand
            - core logic: use a dictionary to count the number of times an element
            shows up. you use bucket sort with an additional list to fill in 
            the values in which each occurence is stored, return the result 
            - input: list of integers
            - output: list of top k elements 
            - edge cases: empty list, list with duplicate values all around 

        2. Plan
            - start off with result list as well as dictionary count of each element
            - also start off with the list that you'll be using for the bucket sort
            - add elements on to the list based on the frequency
            - loop through the elements from descending order


        3. Implement 
        '''

        res = []
        bucket = [[] for i in range(len(nums)+1)]
        new_dict = {}

        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict[num] += 1 

        for n, c in new_dict.items():
            bucket[c].append(n)

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res 