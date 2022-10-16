# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        length = 1
        curr = head
        
        while curr.next:
            length += 1
            curr = curr.next
        
        k %= length
        curr.next = head
        
        for _ in range(length - k):
            curr = curr.next
        
        head = curr.next
        curr.next = None
        
        return head