# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. Understand
            - core logic: traverse through the linked list and remove nth node,
            when removing nth node the idea is to reconstruct the pointers
            - input: head of linked list
            - output: head of linked list with modified values
            - edge cases: empty list, n is greater than length of linked list

        2. Plan
            - set current variable equal to head and begin traversing through
            linked list
            - conditional statement to check whether node is pointing to nth node 
            (node that needs to be removed)
            - redirect the pointers of respective nodes


        3. Implement
        '''

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n>0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next

        

        
         
            