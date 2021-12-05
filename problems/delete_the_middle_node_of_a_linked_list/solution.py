# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        
        while curr:
            curr = curr.next
            n += 1
        
        res = curr = ListNode(-1, head)
        n //= 2
        
        while curr and n > 0:
            curr = curr.next
            n -= 1
        
        if curr and curr.next:
            curr.next = curr.next.next
        
        return res.next