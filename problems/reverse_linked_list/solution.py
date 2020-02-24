# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
    
            
        return prev