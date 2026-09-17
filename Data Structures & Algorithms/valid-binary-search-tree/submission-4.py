# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        1. Understand
            - core logic: Go through the root nodes at each level and compare the 
            values, if the left node is greater than the root node val, return False
            if the right node is less than the root node val, return False
            - input: root (tree)
            - output: boolean
            - edge cases: node.val is equal to the root from either left or right 
            side 

        2. Plan
            - start at the root node and make the base case if the root is None
            return True 
            - recursive case: check the left and right node values


        3. Implement
        '''

        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val,
            right)
        return valid(root, float("-inf"), float("inf"))