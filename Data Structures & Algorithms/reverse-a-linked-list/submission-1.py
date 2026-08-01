# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Understand (input/output, tradeoffs, edge cases)
            - Problem is asking us to take a linked list and reverse the order of the nodes
            - node structure is in the comments for better understanding and potential usage
            - input = an ordered linked list (denoted as head), output = the same linked list but order reversed
            - edge cases: linked list with size 1 or 0

        2. Plan
            - Initialize head as variable. set as current
            - Initialize variable called prev set to None (to keep track of pointer)
            - Loop through the linked list
            - intiailze new variable called new_node and set it equal to current.next
            - set current.next = prev
            - set prev = current (flips the direction of the pointer)
            - set current = new_node to move on and repeat cycle
            - finally return prev as it keeps update of all the cycles seen in list

        3. Implement 
        '''

        current = head
        prev = None

        while current is not None:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        return prev

        
        