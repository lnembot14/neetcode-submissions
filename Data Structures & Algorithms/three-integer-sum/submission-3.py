class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. Understand
            - core logic: go through list and return group of triplets that add
            up to 0.
            - input: list of integers
            - output: list of list of integers
            - edge cases: empty list, no triplet of integers equals to 0

        2. Plan
            - loop through the list 
            - initialize pointers j and k (j at the current index+1 and k at the 
            end of list)
            - you'd keep going until j reaches k 
            - condition for if j+k+i is greater than and condition for if it's less
            than 0
            - declare a list to store triplets in
            - return list 

        3. Implement

        '''
        ordered_nums = sorted(nums)
        triplets = []

        # [-4,-1, -1, 0, 1, 2]
        #  i  j            k 
        

        for i in range(len(ordered_nums)):
            if  i > 0  and ordered_nums[i-1] == ordered_nums[i]:
                continue
            else:
                j = i + 1
                k = len(ordered_nums)-1        
                while j < k:
                    if ordered_nums[i] + ordered_nums[j] + ordered_nums[k] < 0:
                        j += 1
                    elif ordered_nums[i] + ordered_nums[j] + ordered_nums[k] > 0:
                        k -= 1
                    else:
                        triplets.append([ordered_nums[i], ordered_nums[k],
                        ordered_nums[j]])
                        while j<k and  ordered_nums[j] == ordered_nums[j+1]:
                            j += 1
                        while j<k and ordered_nums[k] == ordered_nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1         
        return triplets


        