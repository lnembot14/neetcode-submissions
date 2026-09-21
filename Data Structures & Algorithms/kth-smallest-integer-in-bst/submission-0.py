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
            - core logic: traversing through the tree and checking the kth smallest
            value from each node (maybe another data stucture needed to storevalues) 
            - input: tree (root)
            - output: integer value 
            - edge cases: tree given is not a bst, empty tree

        2. Plan
            - store each value from the BST into a list (iteratively)

        3. Implement 
        '''
        
        n = 0
        stack = []
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
            

        

        