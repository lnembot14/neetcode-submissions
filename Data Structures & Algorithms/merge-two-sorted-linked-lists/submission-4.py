# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Understand
            - core logic: loop through linked list and compare node values as you 
            go, im assuming that you need a dummy node for this type of problem
            - input: two heads (linked lists)
            - output: list merged together
            - edge cases: empty list, list where all elements are the same 

        2. Plan
            - create a dummy node/tail
            - iterate through list and compare node values
            - if you reach the end of one of the lists, attach the other list
            to it to get the remaining values 

        3. Implement
        '''

        dummy = ListNode(0)
        tail = dummy
        

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next


        