class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. Understand
            - core logic: Loop through the list and return list of 3 elements
            where sum of elements add up to 0
            - input: a list of integers
            - output: a list of lists of integers (triplets)
            - edge cases: empty list, no values add up to 0, all numbers in list
            are duplicates

        2. Plan
            - order list
            - intialize triplets list
            - initialize left and right pointers
            - loop through the list
            check if values added together are greater than or less than 0
            if greater than move down
            if less than move up
            - when you find one that equals 0
                - add elements to triplets 
                - check for duplicates and move pointers accordingly
            update pointers
            return triplets

        3. Implement 
        '''

        ordered_list = sorted(nums)
        triplets = []

        for i in range(len(ordered_list)):
            j = i + 1
            k = len(ordered_list) -1 
            if i > 0 and ordered_list[i] == ordered_list[i-1]:
                continue
            while j < k:
                if ordered_list[i] + ordered_list[j] + ordered_list[k] < 0:
                    j += 1
                elif ordered_list[i] + ordered_list[j] + ordered_list[k] > 0:
                    k -= 1
                else:
                    triplets.append([ordered_list[i], ordered_list[j], ordered_list[k]])
                    while j < k and ordered_list[j] == ordered_list[j+1]:
                        j += 1
                    while j < k and ordered_list[k] == ordered_list[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return triplets














