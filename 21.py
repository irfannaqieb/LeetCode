# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy node to initialize the new list
        dummy = ListNode()
        current = dummy

        # Iterate through both the lists
        while list1 and list2:
            if list1.val <list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the current pointer
            current = current.next

        # If there are any remaining elements in either list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the sorted merged list
        return dummy.next
            