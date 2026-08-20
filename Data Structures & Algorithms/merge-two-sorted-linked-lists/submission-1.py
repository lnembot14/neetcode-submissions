# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        1. Understand
            - core logic: going through linked list and linking sorted nodes 
            together based on their places in the respective linked list
            - input: two linked lists 
            - output: new sorted linked list
            - edge cases: empty linked list, linked list with one node, nodes
            have all the same value  

        2. Plan
            - declare a new linked list variable
            - 


        3. Implement
        '''
        
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val < list2.val:
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
            
        return res.next


        

        


        
        