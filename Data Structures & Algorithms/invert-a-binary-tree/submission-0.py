# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        1. Understand
            - core logic: Essentially taking the left branch or side of the tree
            and attaching it to the right, vice versa
            - input: originally sorted root or linked list
            - output: linked list with switched branches
            - edge cases: empty tree

        2. Plan
            - traverse through tree
            - try and find a way to make the root.left = root.right and root.right =
            root.left

        3. Implement
        '''

        if not root:
            return None
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

            