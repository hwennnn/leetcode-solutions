# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        front = cFront = ListNode(-1)
        back = cBack = ListNode(-1)
        
        while head:
            v = head.val
            if v < x:
                front.next = ListNode(v)
                front = front.next
            else:
                back.next = ListNode(v)
                back = back.next
            
            head = head.next
        
        front.next = None
        front.next = cBack.next
        
        return cFront.next