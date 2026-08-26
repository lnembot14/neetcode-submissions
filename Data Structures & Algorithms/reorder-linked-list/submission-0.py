# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. Understand
            - core logic: reordering the nodes of the linked list, going through the
            list and swapping nodes (not the values inside the nodes)
            - input: linked list or head
            - output: modified linked list 
            - edge cases: list of length 1, empty list

        2. Plan
            - iterate through the linked list with current variable
            - find length of linked list
            - iterate again to re order list

        3. Implement
        '''
        #find slow and fast pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    

        #reverse through linked list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        #merge parts of linked list
        first = head
        second = prev
        while second:
            tmp1 = first.next 
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1 
            second = tmp2
        