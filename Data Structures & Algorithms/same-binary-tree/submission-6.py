# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1. Understand
            - core logic: you're recursively going through each node in the tree
            and determining whether or not they share the same structure and or values
            - input: two tree nodes, p and q
            - output: boolean
            - edge cases: empty tree, tree with one node

        2. Plan
            - start at the root node
            - compare the values and structures of the left and right nodes
                - if one empty return false
                - if not continue
            - return boolean 

        3. Implement
        '''

        if not p and not q:
            return True
        if p and not q or not p and q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        