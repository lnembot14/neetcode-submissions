# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
            1. Understand (output/input, edge cases)
                - input: Given two binary trees, output: return boolean on whether
                the two trees are equivalent
                - Note: must be equivalent in terms of node values AND structures
                - edge cases: trees with same values but not the same structure, empty tree,
                tree with no children

            2. Plan
                - Perform pre order traversal, with one of the trees, then compare that
                value to the other tree as pre order traversal is usually just a copy of the said tree

            3. Implement 
        ''' 
        if p is None and q is None:
            return True
        elif p and q is None or q and p is None:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val


        
        
        