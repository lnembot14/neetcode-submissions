# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Understand (core logic, input, output, edge cases)
            - go through the linked list and keep track of nodes visited,
            if you happen to fall across another node, then return true, if 
            not return false 
            - input: head of linked list
            - outptu: boolean
            - edge cases: no cycle in linked list, head contains only one node,
            multiple cycles within list

        2. Plan 
        - create a list
        - loop through the nodes in liked list and add them on to list created
        - if item has already been seen then return true, if not and you go
        through every node, return false

        3. Implement
        '''

        
 
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            



        