class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. Understand
            - input: a list of integers
            - output: list of a list with triplet integers that add up to 
            0 
            - edge cases: no numbers in the list of integers add up to 0, 
            empty list, list contains less than three elements 
            - checking through different triplets (3 elements) in list and 
            returning if the value is equal to 0. 

        2. Plan
            - sort through list
            - loop through the list -2 (save space for j and k)
            - set pointers for j and k
            - check while j < k, if any duplicates occur
            - then you want to add i, j and k, if the value is higher than 0, 
            reduce k by 1
            - if the value is lower than 0 increment j by 1 


        3. Implement

        '''
        
        
        

        new_list = sorted(nums)
        triplets = []

        for i in range(len(new_list) -2):
            j = i + 1
            k = len(new_list) -1
            if i > 0 and new_list[i] == new_list[i-1]:
                    continue 
            while j < k:
                if new_list[i] + new_list[j] + new_list[k] > 0:
                    k-= 1
                elif new_list[i] + new_list[j] + new_list[k] < 0:
                    j += 1
                else: 
                    triplets.append([new_list[i], new_list[j], new_list[k]])
                    while j < k and new_list[j] == new_list[j+1]:
                        j += 1
                    while j < k and new_list[k] == new_list[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return triplets 
