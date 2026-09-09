# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        1. Understand
            - core logic: keeping track of the amount nodes between the longest
            set of nodes
            - input: root (tree)
            - output: integer (max number of depth)
            - edge cases: empty tree, tree with one node 

        2. Plan 
            - set a variable max 
            - go through tree and keep count of the path between root to each node
            - return the max variable in some type of way

        3. Implement
        '''

        if not root:
            return 0
        else:
            max_right = 1 + self.maxDepth(root.right)
            max_left = 1 + self.maxDepth(root.left)
            return max(max_left, max_right)

        