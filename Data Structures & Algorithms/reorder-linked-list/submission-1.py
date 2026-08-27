# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. Understand 
            - core logic: using fast and slow pointers to switch the order of the
            linked list while splitting the list into parts based on the pointers
            - input: head of linked list
            - output: modified linked list
            - edge cases: odd length linked list, empty list

        2. Plan 
            - initialize fast and slow pointers to find middle point of the list
            - reverse the second part of the list
            - merge two lists together 

        3. Implement 
        '''

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        #merge lists together
        
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            

        

        