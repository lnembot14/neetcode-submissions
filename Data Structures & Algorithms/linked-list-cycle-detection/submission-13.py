# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Understand
            - core logic: need to find whether the one of the nodes of the linked
            list points to another node that was already explored (creating a cycle)
            - input: head of linked list
            - output: boolean
            - edge cases: one node in linked list, empty list

        2. Plan
            - set a variable node
            - loop through the linked list with two pointers, one being the
            a slower head (moves one step) and the other being a faster head (moves
            two steps)
            - check if nodes meet and return boolean

        3. Implement 
        '''

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        