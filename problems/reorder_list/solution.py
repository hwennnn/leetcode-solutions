# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev
    
    def mergeLL(self, l1, l2):
        while l1:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            
            if not n1: break
            
            l2.next = n1
            l1 = n1
            l2 = n2
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        
        prev, slow, fast, l1 = None, head, head, head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        l2 = self.reverseLL(slow)

        self.mergeLL(l1, l2)