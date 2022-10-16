# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            
            if count == k:
                prev, curr = r, l
                for _ in range(k):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                    
                dummy.next, dummy, l = prev, l, r
            else:
                return res.next
            