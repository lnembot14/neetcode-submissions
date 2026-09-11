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
            - core logic: You're given a binary tree with a left root and a right 
            root, the goal is to swap nodes at each level of the tree (recursively)
            - input: root 
            - output: modified root with nodes switched
            - edge cases: empty list

        2. Plan 
            - base case essentially asking if our root is None
            - at each iteration of the tree we're swapping the nodes using a
            temporary variable
            - recursively call the function again so we can continue to swap
            - return root

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
        