# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Understand
        - core logic: Take a linked list that begins at head and return a list with the
        values in reverse (indicates switching the pointers)
        - input : list
        - output: list but with values reversed
        - edge case: empty list or list with one element (unusual to reverse)


        2. Plan 
        - variables (prev, current, head)
        - traverse through the linked list
        - set the head 


        3. Implement
        '''


        current = head
        prev = None
        while current != None:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        return prev
        