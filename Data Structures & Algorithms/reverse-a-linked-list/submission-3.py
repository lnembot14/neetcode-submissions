# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Understand
            - core logic: traversing through the linked list and returning a 
            reversed version of it
            - input: head of linked list
            - output: same linked list, reversed order
            - edge case: empty list, list with one character, 

        2. Plan
            - traverse through linked list (set current = head)
            - set variable prev
            - set the current.next's node to prev
            - set prev = current
            - continue to iterate through list with current = current.next


        3. Implement
        '''

        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        