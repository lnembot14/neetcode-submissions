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
            - core logic: a certain threshold that needs to be held between all
            of the nodes starting from the root. (left < node < right). If a value 
            from either the left or right doesn't validate the rule, return False
            - input: binary tree or root
            - output: boolean
            - edge cases: empty tree, tree with all of the same nodes 

        2. Plan
            - helper function valid

        3. Implement
        '''

        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
        