# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Understand (input, output, core logic)
            - input: head of a linked list
            - output: boolean
            - core logic: Need a way to go through the linked list and its nodes perhaps 
            with two pointers, a fast and a slow one, if the fast one meets up with the 
            slow one, it means that there is a cycle

        2. Plan
            -initialize a slow and fast pointer
            - loop through the linked list (check if the head's next still exists or
            its head exists)
            - check if the slow pointer's node is equal to the fast pointer's node at any point
                - return true
            - if not return false

        3. Implement
        '''
        slow = head
        fast = head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 
