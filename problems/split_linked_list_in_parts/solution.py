# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        
        curr = head
        while curr:
            curr = curr.next
            length += 1
            
        res = [None] * k
        curr, prev = head, None
        n, r = length // k, length % k
        i = 0
        
        while curr and i < k:
            res[i] = curr
            
            for _ in range(n):
                prev = curr
                curr = curr.next
            
            if i + 1 <= r:
                prev = curr
                curr = curr.next
            
            prev.next = None
            i += 1
        
        return res