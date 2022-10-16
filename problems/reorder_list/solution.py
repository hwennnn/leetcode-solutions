# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        def reverseLL(curr):
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        head2 = reverseLL(p1.next)
        p1.next = None
        
        while head and head2:
            tmp1 = head.next
            tmp2 = head2.next
            head2.next = head.next
            head.next = head2
            head = tmp1
            head2 = tmp2
        
        