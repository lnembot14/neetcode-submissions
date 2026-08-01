# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        1. Understand (core logic, input, output, edge cases)
            - input: head of linked list 
            - output: boolean
            - core logic: Go through each and every single node in linkedlist
            to determine whether or not any of it's pointers point to an existing node.
            Once we find something like that, it's time to return true 
            - edge cases: only one singular node or node is null

        2. Plan 
            - initialize slow and fast pointers to head
            - loop through linked list (check if the fast node is null or its pointer is null)
            - check if slow and fast node are equal, if they are then return True
            - if not continue moving both pointers, 
            - add a false statement outside the loop if nodes never meet

        3. Implement 

        '''

        slow = head
        fast = head 

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False 
        