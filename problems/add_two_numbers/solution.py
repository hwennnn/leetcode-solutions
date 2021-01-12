# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = res = ListNode(-1)
        carry = 0
        
        while l1 or l2 or carry:
            if l1: 
                carry += l1.val
                l1 = l1.next
                
            if l2:
                carry += l2.val
                l2 = l2.next
            
            v = carry % 10
            carry //= 10
    
            node = ListNode(v)
            curr.next = node
            curr = curr.next
            
        return res.next
            