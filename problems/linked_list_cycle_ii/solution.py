# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return None
        
        t = h = curr = head
        
        while h and h.next:
            
            t = t.next
            h = h.next.next
            
            if t == h:
                while curr != h:
                    curr = curr.next
                    h = h.next
                    
                return h
        
        return None