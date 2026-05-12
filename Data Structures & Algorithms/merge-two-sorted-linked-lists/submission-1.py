# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         
        dummy = ListNode() # create a placeholder node with value 0 
        ptr = dummy # set a pointer to the node 

        while list1 and list2: # make sure list1 and list2 aren't null
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2 
                list2 = list2.next

            ptr = ptr.next
        
        if list1: 
            ptr.next = list1
        elif list2:
            ptr.next = list2
        
        return dummy.next





