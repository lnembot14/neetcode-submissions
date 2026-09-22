# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        1. Understand
            - core logic: iterating through list and adding elements to the stack
            based on the value of the node. matching k with the specific value
            - input: root
            - output: integer
            - edge cases: empty list, given a non BST

        2. Plan
            - declare stack and n variable to keep track
            - loop through the stack and current variable
            - under that loop, loop through the current

        3. Implement 
        '''

        stack = []
        n = 0 
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n += 1
            if n == k:
                return current.val
            current = current.right

        