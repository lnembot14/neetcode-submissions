class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Understand
            - core logic: going through all of the elements in the list and 
            keeping track of how many times they appear in the list 
            - input: array of integers
            - output: an array of the top k elements (slicing maybe)
            - edge cases: empty list, all integers from the list are the same 

        2. Plan
            - declare a dictionary to keep track of all of the integers and amount 
            of times they appear in the list

        3. Implement 
        '''
        
        freq_dict = {}
        freq_list = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        
        for n,c in freq_dict.items():
            freq_list[c].append(n)
        
        res = []

        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res 




        



        
