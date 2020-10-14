# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev, c = dummy, head
        
        for i in range(m-1):
            prev = prev.next
            c = c.next
        
        r = None
        for _ in range(n-m+1):
            tmp = c
            c = c.next
            tmp.next = r
            r = tmp
        
        prev.next.next = c
        prev.next = r
        
        return dummy.next