# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                p = curr.next
                val = p.val
                while p and p.val == val:
                    p = p.next
                curr.next = p
            else:
                curr = curr.next
        
        return dummy.next