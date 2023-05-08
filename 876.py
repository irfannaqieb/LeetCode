# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = slow = head

        while fast:
            if not fast.next:
                break
        
            fast = fast.next.next
            slow = slow.next

        return slow