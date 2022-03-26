# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        curr = res = ListNode(-1)
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            
            if s2:
                carry += s2.pop()
            
            curr.next = ListNode(carry % 10)
            curr = curr.next
            
            carry //= 10
        
        def reverseLL(head):
            prev = None
            
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            
            return prev
        
        return reverseLL(res.next)
        