# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        1. Understand
            - core logic: creating a dummy node and attaching the first node and
            onwards based on condition
            - input: two linked lists
            - output: linked list merged together
            - edge cases: empty list, one list is larger in size than the other,
            nodes all have equal values
        2. Plan
            - create the dummy node


        3. Implement
        '''
        
        dummy = ListNode()
        tail = dummy


        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list2:
            tail.next = list2
        elif list1:
            tail.next = list1
        return dummy.next

