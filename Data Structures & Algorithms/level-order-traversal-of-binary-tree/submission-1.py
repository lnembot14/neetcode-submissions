# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        1. Understand
            - core logic: you have a queue that keeps track of each node from the
            tree, you go level by level trying to examine the amount of nodes
            per level. You pop that node from the queue add its children nodes
            if it has any and append it onto the level list, level list at that
            iteration gets added on to the result list
            - input: tree root node
            - output: 2d list
            - edge cases: empty list

        2. Plan 
            - declare res and queue
            - append the root node onto queue
            - loop while queue is empty
            - declare level an the queue length to inidcate how many nodes to add
            onto the level list
            - pop the node at the front of the queue, if node is not empty, append
            it onto level, and add its left and right children
            - to make sure of no empty lists in the solution, use an if level to add
            all non empty lists to result 

        3. Implement

        '''

        queue = collections.deque()
        res = []
        queue.append(root)

        while queue:
            queue_len = len(queue)
            level = []
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res 
        