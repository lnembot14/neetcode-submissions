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
            - core logic: from the root node, you're going down the left and right
            tree and swapping the values from each with one another
            - input: root node (tree)
            - output: modified root node
            - edge cases: empty tree, unbalanced tree

        2. Plan
            - iterate recursively through the tree
            - use a temporary variable to store the nodes from either left or right
            tree
            - swap the values
            - then call recursive state
            - return root 

        3. Implement
        '''

        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root 
        