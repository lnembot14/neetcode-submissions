# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. Understand
            - core logic:  
            - input: tree root, subtree p and subtree q
            - output: lowest common ancestor of p and q as an integer
            - edge cases: empty tree, trees don't share any nodes

        2. Plan
            - 

        3. Implement
        '''

        current = root

        while current:
            if p.val < current.val and q.val > current.val or p.val > current.val and q.val < current.val:
                return current
            if p.val == current.val or q.val == current.val:
                return current
            else:
                if q.val > current.val and p.val > current.val:
                    return self.lowestCommonAncestor(root.right, p, q)
                elif p.val < current.val and q.val < current.val:
                    return self.lowestCommonAncestor(root.left, p, q)
        return current
    



